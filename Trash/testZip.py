import os
import zipfile

def rebuild_docx_from_folder(folder_path, output_docx):
    with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as docx:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = file.replace('_', '/')
                docx.write(file_path, arcname)
                print(f"[+] Ajouté : {file_path} -> {arcname}")
    print(f"\n[*] Nouveau fichier .docx créé : {output_docx}")

# Exemple d'utilisation
if __name__ == "__main__":
    folder = "extracted_xml"  # Le dossier contenant tes .xml extraits et modifiés
    output_file = "modified_victim.docx"
    rebuild_docx_from_folder(folder, output_file)

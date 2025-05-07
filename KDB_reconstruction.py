import base64

# Lis le fichier base64
with open("vault.b64", "r", encoding="utf-8") as f:
    b64_data = f.read()

try:
    # Nettoie et décode la base64
    binary_data = base64.b64decode(b64_data)

    # Écris le fichier binaire
    with open("vault.kdbx", "wb") as out_file:
        out_file.write(binary_data)

    print("[+] Fichier vault.kdbx reconstruit avec succès.")
except Exception as e:
    print("[-] Erreur pendant la conversion :", e)

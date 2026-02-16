import threading
from pykeepass import PyKeePass
from queue import Queue
from tqdm import tqdm

# Paramètres
VAULT_PATH = 'vault.kdbx'
WORDLIST_PATH = 'wordlists/fr-top1000000.txt' 
NUM_THREADS = 10

with open(WORDLIST_PATH, 'r', encoding='utf-8', errors='ignore') as f:
    passwords = [line.strip() for line in f if line.strip()]

password_queue = Queue()
for pwd in passwords:
    password_queue.put(pwd)

found_flag = threading.Event()
found_password = {'value': None}

progress = tqdm(total=len(passwords), desc="Bruteforcing", ncols=80)

def worker():
    while not password_queue.empty() and not found_flag.is_set():
        password = password_queue.get()
        try:
            kp = PyKeePass(VAULT_PATH, password=password)
            found_password['value'] = password
            found_flag.set()
        except:
            pass
        finally:
            progress.update(1)
            password_queue.task_done()

threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

progress.close()

if found_password['value']:
    print(f"[+] Mot de passe trouvé : {found_password['value']}")
else:
    print("[-] Aucun mot de passe trouvé.")

import zipfile

def crack_zip_password(zip_file, wordlist_file):
    with open(wordlist_file, 'r') as wordlist:
        passwords = wordlist.readlines()

    for password in passwords:
        password = password.strip()

        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(pwd=password.encode('utf-8'))
            print(f"Le mot de passe a été trouvé: {password}")
            return
        except zipfile.BadZipFile:
            print("Le fichier zip est corrompu.")
            return
        except Exception:
            continue

    print("Le mot de passe n'a pas été trouvé dans la liste fournie.")


if __name__ == '__main__':
    zip_file = input("Entrez le chemin du fichier zip: ")
    wordlist_file = input("Entrez le chemin du fichier wordlist: ")
    crack_zip_password(zip_file, wordlist_file)
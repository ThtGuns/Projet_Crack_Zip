import os

def generate_wordlist(wordlist_file, max_length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+=~`[]{}|\\:;\"'<>?,./"

    with open(wordlist_file, 'w') as f:
        for length in range(1, max_length + 1):
            generate_wordlist_recursive(f, '', characters, length)


def generate_wordlist_recursive(file, prefix, characters, length):
    if length == 0:
        file.write(prefix + '\n')
        return

    for char in characters:
        generate_wordlist_recursive(file, prefix + char, characters, length - 1)


if __name__ == '__main__':
    wordlist_file = input("Entrez le chemin du fichier wordlist à générer: ")
    max_length = int(input("Entrez la longueur maximale des mots de passe: "))
    generate_wordlist(wordlist_file, max_length)
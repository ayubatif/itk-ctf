import fileinput

def encrypt_letter(key, letter):
    if not letter.isalpha(): return letter
    char = ord(letter) + (key - ord("A"))
    if char > ord("Z"):
        char -= (ord("Z") - ord("A") + 1)
    return chr(char)

def decrypt_letter(key, letter):
    if not letter.isalpha(): return letter
    char = ord(letter) - (key - ord("A"))
    if char < ord("A"):
        char += (ord("Z") - ord("A") + 1)
    return chr(char)

def encrypt(text):
    key = ord(text[0])
    encr_text = text[0]
    text = text[1:]
    for letter in text:
        encr_text += encrypt_letter(key, letter)
    return encr_text

def decrypt(text):
    key = ord(text[0])
    decr_text = ""
    text = text[1:]
    for letter in text:
        decr_text += decrypt_letter(key, letter)
    return decr_text

for line in fileinput.input():
    print(decrypt(line))
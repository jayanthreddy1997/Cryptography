
def encrypt_vigenere(plain_text: str, key: str) -> str:
    cipher = ''
    for i in range(len(plain_text)):
        cipher += chr(ord(plain_text[i]) + ord(key[i%len(key)]) - ord('a'))

    print(f'Encrypted vigenere cipher is {cipher}')
    return cipher


def decrypt_vigenere(cipher_text: str, key: str) -> str:
    plain_text = ''

    for i in range(len(cipher_text)):
        plain_text += chr(ord(cipher_text[i]) - (ord(key[i % len(key)]) - ord('a')))

    print(f'Decrypted plaintext is {plain_text}')
    return plain_text


if __name__ == '__main__':
    key = "big"
    cipher_text = encrypt_vigenere(plain_text="hello@world2", key=key)
    decrypt_vigenere(cipher_text, key=key)



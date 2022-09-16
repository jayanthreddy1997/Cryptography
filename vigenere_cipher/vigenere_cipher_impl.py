
def encrypt_vigenere_cipher(plain_text: str, key: str) -> str:
    """
    Encrypt plain text based on Vigenere cipher algorithm
    :param plain_text: Plain text using english alphabet
    :param key: Integer key to encrypt the plain text
    :return: Encrypted cipher text
    """
    cipher = ''

    for i in range(len(plain_text)):
        cipher += chr(ord(plain_text[i]) + ord(key[i%len(key)]) - ord('a'))

    print(f'Encrypted vigenere cipher is {cipher}')
    return cipher


def decrypt_vigenere_cipher(cipher_text: str, key: str) -> str:
    """
    Decrypt cipher text based on Vigenere cipher algorithm
    :param cipher_text: Cipher text
    :param key: Integer key to decrypt the cipher text
    :return: Decrypted plain text
    """
    plain_text = ''

    for i in range(len(cipher_text)):
        plain_text += chr((ord(cipher_text[i]) - ord(key[i % len(key)])) % 26 + ord('a'))

    print(f'Decrypted plaintext is {plain_text}')
    return plain_text


def main():
    key = "big"
    cipher_text = encrypt_vigenere_cipher(plain_text="helloworldagain", key=key)
    decrypt_vigenere_cipher(cipher_text, key=key)


if __name__ == '__main__':
    main()

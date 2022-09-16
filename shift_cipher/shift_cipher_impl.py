
def encrypt_shift_cipher(plain_text: str, key: int) -> str:
    """
    Encrypt plain text based on shift cipher algorithm
    :param plain_text: Plain text using english alphabet
    :param key: Integer key to encrypt the plain text
    :return: Encrypted cipher text
    """
    cipher_text = ''

    for i in range(len(plain_text)):
        cipher_text += chr(((ord(plain_text[i]) + key - ord('a')) % 26) + ord('a'))

    print(f'Encrypted shift cipher is {cipher_text}')
    return cipher_text


def decrypt_shift_cipher(cipher_text: str, key: int) -> str:
    """
    Decrypt cipher text based on shift cipher algorithm
    :param cipher_text: Cipher text
    :param key: Integer key to decrypt the cipher text
    :return: Decrypted plain text
    """
    plain_text = ''

    for i in range(len(cipher_text)):
        plain_text += chr(((ord(cipher_text[i]) - key - ord('a')) % 26) + ord('a'))

    print(f'Decrypted plaintext is {plain_text}')
    return plain_text


def main():
    key = 4
    cipher_text = encrypt_shift_cipher(plain_text="helloworld", key=key)
    decrypt_shift_cipher(cipher_text, key=key)


if __name__ == '__main__':
    main()

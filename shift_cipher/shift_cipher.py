
def encrypt_shift(plain_text: str, key: int) -> str:
    cipher_text = ''
    for i in range(len(plain_text)):
        cipher_text += chr(ord(plain_text[i]) + key)

    print(f'Encrypted shift cipher is {cipher_text}')
    return cipher_text


def decrypt_shift(cipher_text: str, key: int) -> str:
    plain_text = ''

    for i in range(len(cipher_text)):
        plain_text += chr(ord(cipher_text[i]) - key)

    print(f'Decrypted plaintext is {plain_text}')
    return plain_text


def main():
    key = 4
    cipher_text = encrypt_shift(plain_text="hello@world!", key=key)
    decrypt_shift(cipher_text, key=key)


if __name__ == '__main__':
    main()

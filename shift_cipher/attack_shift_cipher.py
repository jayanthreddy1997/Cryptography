from utils.constants import ENGLISH_CHAR_PROB


def get_shift_cipher_key(cipher_text):
    cipher_text = cipher_text.lower()
    cipher_char_prob = {}

    for i in range(len(cipher_text)):
        if cipher_text[i] not in cipher_char_prob:
            cipher_char_prob[cipher_text[i]] = 0.
        cipher_char_prob[cipher_text[i]] += 1.
    for k, v in cipher_char_prob.items():
        cipher_char_prob[k] = v/len(cipher_text)

    I = []
    for key_ in range(26):
        curr_sum = 0.
        for j in range(26):
            curr_sum += ENGLISH_CHAR_PROB[chr(ord('a') + j)] * cipher_char_prob.get(chr(ord('a') + j + key_), 0)
        I.append(curr_sum)

    # Finding key which generates distribution closest to english alphabet
    I = [abs(x-0.065) for x in I]
    key = I.index(min(I))
    print(f'Identified key as {key}')
    return key


def decrypt_shift_cipher(k, cipher_text):
    cipher_text = cipher_text.lower()
    plain_text = ''

    for i in range(len(cipher_text)):
        plain_text += chr(((ord(cipher_text[i]) - k - ord('a')) % 26) + ord('a'))

    print(f'Decrypted text for key {k} and ciphertext {cipher_text} is {plain_text}')
    return plain_text


if __name__ == '__main__':
    cipher_text = 'OVDTHUFWVZZPISLRLFZHYLAOLYL'
    k = get_shift_cipher_key(cipher_text)
    decrypt_shift_cipher(k, cipher_text)

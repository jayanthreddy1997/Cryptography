from utils.constants import ENGLISH_CHAR_PROB
from shift_cipher.shift_cipher_impl import decrypt_shift_cipher


def get_shift_cipher_key(cipher_text: str) -> int:
    """
    Function to recover the key based on the cipher text
    :param cipher_text: Cipher text in english alphabet
    :return: Recovered key
    """
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


def main():
    cipher_text = 'OVDTHUFWVZZPISLRLFZHYLAOLYL'
    key_ = get_shift_cipher_key(cipher_text)
    decrypt_shift_cipher(cipher_text.lower(), key_)


if __name__ == '__main__':
    main()

from utils.constants import ENGLISH_CHAR_PROB
from vigenere_cipher.vigenere_cipher_impl import decrypt_vigenere_cipher


def get_vigenere_cipher_key(cipher_text: str) -> str:
    """
    Function to recover the key based on the cipher text
    :param cipher_text: Cipher text in english alphabet
    :return: Recovered key
    """
    # Part1: Identify the key length (using index of coincidence algorithm)
    key_length = -1
    min_diff = 1
    for m in range(1, 10):
        subseq = cipher_text[::m]
        freq_table = [0]*26
        for c in subseq:
            freq_table[_get_integer_encoding(c)] += 1.
        freq_table = [x/len(subseq) for x in freq_table]
        curr_diff = abs(0.065 - sum([x**2 for x in freq_table]))
        if curr_diff < min_diff:
            min_diff = curr_diff
            key_length = m

    print(f'Identified key length as {key_length}')

    # Part2: Recover the key
    key = ''
    for i in range(key_length):
        subseq = cipher_text[i::key_length]
        freq_table = [0] * 26
        for c in subseq:
            freq_table[_get_integer_encoding(c)] += 1.
        freq_table = [x / len(subseq) for x in freq_table]

        I = []
        for j in range(26):
            curr_sum = 0.
            for x in range(26):
                curr_sum += ENGLISH_CHAR_PROB[chr(x+ord('a'))] * freq_table[(j+x)%26]
            I.append(curr_sum)
        temp = [abs(y-0.065) for y in I]
        k = chr(temp.index(min(temp)) + ord('a'))
        key += k

    print(f'Identified key as "{key}"')
    return key


def _get_integer_encoding(c):
    return ord(c) - ord('a')


def main():
    cipher_text = 'khrxbukeqvhmkefrtmdeelqmtozpczcyxqcieafwvqlnvwspjtnwsefrnpsdzcnlgmkrnqgofnglbqetnoqalngumxfcnwspgr' \
                  'vpodzlllbzfrgkoyvrvfoukcbqgujtfrtrzfgbgfrtrvorvdruoxuifwfuttsljqdawrfgeiafcdgoedhqutrufukoelseeiah' \
                  'aueoerifcyvquujlnqrernqwvdveuxbpieqwkqetlvwjznqloziefhfhrtvrbenigkzudighrefvrusuxngbwfzsgksfyiegzm' \
                  'igrvhofuawfksyorhtcaagozutbwoxrrrdhtvualhqusgdhqjsudfqjlnqrnfrqhfenigkqmeaqdhaztfqcdkhnqriztupsjzc' \
                  'bwcuksfrifyigpouetnlbedaelhudeorfpvrfzwfytuhpmyazdgolbnuiejindbpftuhfzrtvrbeztudgmgocxzmkibqcrfvru' \
                  'htierkizurrgozutulffpoahauclvrbmedvvhtvtulfpdofwdaguyrietohqhdpiawvqnoeormwtruqtznndbpznqlofyeadhu' \
                  'fnnoqmgigdzujwnvvueggrbptaaghtvmbvhbfphocgjcvwmmedslbmecvdzovnghfujnrzmaikplhkkhrxbukeqvhmkeflgmde' \
                  'ywwzxpbwcrtuywidvsnqrqkhalqukirvozuigvdaguydhufnudgnveasfawohqrxpsuddqublfszkuelseffvpauxrnwwaeigk' \
                  'oerhvjvxpdvysdjepowyrtrdbpxebjfmghldbpzsbitutinozkiepruzzzrgoefnrrtfyefhjqetrhbqtoyruutayomyvgngwh' \
                  'vrfhqalnguwqj'
    k = get_vigenere_cipher_key(cipher_text)
    decrypt_vigenere_cipher(cipher_text, k)


if __name__ == '__main__':
    main()

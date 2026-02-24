import numpy as np


class Assignment3_1:
    def __init__(self):    
        self.english_alphabet_map = {
            "A": 0, "N": 13,
            "B": 1, "O": 14,
            "C": 2, "P": 15,
            "D": 3, "Q": 16,
            "E": 4, "R": 17,
            "F": 5, "S": 18,
            "G": 6, "T": 19,
            "H": 7, "U": 20,
            "I": 8, "V": 21,
            "J": 9, "W": 22,
            "K": 10, "X": 23,
            "L": 11, "Y": 24,
            "M": 12, "Z": 25
        }


    # ! here key is a m x m matrix
    # given key is a 2 x 2 matrix so m = 2
    def encryption(self, plaintext:str = 'hello', key = [[11, 8], [12, 9]]) -> str:
        encoded: str= ''

        # due to the key being 2 x 2 and the length of plaintext being 5 => padding must be done after splitting in groups of 2 characters
        group1 = 'he'
        group2 = 'll'
        
        # use x as padding
        group3 = 'ox'

        groups = [group1.upper(), group2.upper(), group3.upper()]

        for group in groups:
            ch1 = group[0]
            ch2 = group[1]

            # numerical representation of each character
            ch1_numerical = self.english_alphabet_map[ch1]
            ch2_numerical = self.english_alphabet_map[ch2]

            # numerical representation of encoded characters
            # encoded numerical is an array of length 2
            encoded_numerical = np.matmul((ch1_numerical, ch2_numerical), key) % 26

            # transform encoded numerical into encoded (i.e. as string)
            ch1_encoded_numerical = encoded_numerical[0]
            ch2_encoded_numerical = encoded_numerical[1]

            ch1_encoded_character, = [k for k, v in self.english_alphabet_map.items() if v == ch1_encoded_numerical]
            ch2_encoded_character, = [k for k, v in self.english_alphabet_map.items() if v == ch2_encoded_numerical]

            encoded_group = ch1_encoded_character + ch2_encoded_character

            encoded += encoded_group
        
        return encoded

def main():
    encrypter = Assignment3_1()
    print(f'The encoding of hello is: {encrypter.encryption()}')


if __name__ == '__main__':
    main()
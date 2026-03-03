import math


class Assignment3_3:
    def __init__(self):
        # Z = 26
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
    
    # key is a 2 x 2 matrix => split into groups of 2
    def encryption(self, c11: int, c12: int, c21: int, c22: int, plaintext: str) -> str:
        key = [[c11, c12], [c21, c22]]

        # determinant
        det_key = c11 * c22 - c12 * c21

        # 1. check if det(key) != 0
        if int(det_key) == 0:
            raise Exception('The determinant of the key is equal to 0!')
        
        # 2. check if gcd(det(key), 26) == 1
        if math.gcd(det_key, 26) != 1:
            raise Exception('The determinant of the matrix should be relative prime to 26 (i.e.: gcd(det, 26) == 1)')
        
        encoded: str = ''

        plaintext = plaintext.upper()
        
        # len(plaintext) % 2 == 1 => padding is needed
        if len(plaintext) % 2 == 1:
            plaintext += 'X'
        
        a = key[0][0]
        b = key[0][1]
        c = key[1][0]
        d = key[1][1]

        for index in range(0, len(plaintext), 2):
            ch1 = plaintext[index]
            ch2 = plaintext[index + 1]
            
            # numerical representation of each character
            ch1_numerical = self.english_alphabet_map[ch1]
            ch2_numerical = self.english_alphabet_map[ch2]

            # numerical representation of encoded characters
            encoded_ch1 = (ch1_numerical * a + ch2_numerical * c) % 26
            encoded_ch2 = (ch1_numerical * b + ch2_numerical * d) % 26

            # convert back to letters
            ch1_encoded_character, = [k for k, v in self.english_alphabet_map.items() if v == encoded_ch1]
            ch2_encoded_character, = [k for k, v in self.english_alphabet_map.items() if v == encoded_ch2]

            encoded_group = ch1_encoded_character + ch2_encoded_character

            encoded += encoded_group
        
        return encoded

def main():
    
    plaintext = input('Enter the desired plaintext: ')
    print('''
        Next up, you will need to enter the coordinates of a matrix of this form:
          (c11, c12)
          (c21, c22)

    ''')
    c11 = int(input('Enter a value for c11: '))
    c12 = int(input('Enter a value for c12: '))
    c21 = int(input('Enter a value for c21: '))
    c22 = int(input('Enter a value for c22: '))
    
    encrypter = Assignment3_3()

    encoded = encrypter.encryption(c11, c12, c21, c22, plaintext)

    print(f'The encryption of {plaintext} using the key [[{c11}, {c12}], [{c21}, {c22}]] is: {encoded}')


if __name__ == '__main__':
    main()
import math


class Assignment2_1:
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


    def encryption(self, a: int, b: int, plaintext: str) -> str:
        if math.gcd(a, 26) != 1:
            raise Exception(f'Chose a, such that gcd(a, 26) = 1 !')
        
        encoded: str = ''
        for character in plaintext:
            if character not in self.english_alphabet_map:
                continue
            # numerical representation of the character
            character_numerical = self.english_alphabet_map[character]

            # numerical representation of the encoded character
            encoded_numerical = (a * character_numerical + b) % 26

            # transform encoded numerical into encoded (i.e. as string)
            encoded_character, = [k for k, v in self.english_alphabet_map.items() if v == encoded_numerical]

            encoded += encoded_character
        
        return encoded


def main():
    user_input = input('Enter the plaintext: ')
    a = int(input('Enter a value for a (numerical < 26): '))
    b = int(input('Enter a value for b (numerical < 26): '))

    encrypter = Assignment2_1()

    encoded = encrypter.encryption(a, b, user_input.upper())

    print(f'The encoded string is: {encoded}')

if __name__ == '__main__':
   main()

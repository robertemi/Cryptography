import math


class Assignment2_2:
    def __init__(self):
        # used for computing a prime (a')
        # for the english alphabet m = 26
        self.m = 26

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

    def compute_a_prime(self, a: int) -> int:
        for a_prime in range(0, 26):
            if (a * a_prime - 1) % 26 == 0:
                return a_prime
        
        return None


    def decryption(self, a: int, b: int, ciphertext: str) -> str:
        if math.gcd(a, 26) != 1:
            raise Exception(f'Chose a, such that gcd(a, 26) = 1 !')
        
        decoded: str = ''
        for character in ciphertext:
            if character not in self.english_alphabet_map:
                continue
            # numerical representation of the character
            encoded_numerical = self.english_alphabet_map[character]

            # numerical representation of the decoded character
            decoded_numerical = self.compute_a_prime(a) * (encoded_numerical - b) % 26

            # transform decoded numerical into decoded (i.e. as string)
            decoded_character, = [k for k, v in self.english_alphabet_map.items() if v == decoded_numerical]

            decoded += decoded_character
        
        return decoded

def main():
    user_input = input('Enter the ciphertext: ')
    a = int(input('Enter a value for a (numerical < 26): '))
    b = int(input('Enter a value for b (numerical < 26): '))

    decrypter = Assignment2_2()

    decoded = decrypter.decryption(a, b, user_input.upper())

    print(f'The decoded string is: {decoded}')


if __name__ == '__main__':
    main()

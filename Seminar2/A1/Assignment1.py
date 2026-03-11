
class Assignment1:

    def __init__(self):
        self.english_alphabet_map_extended = {
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
            "M": 12, "Z": 25,
            "0": 26, "1": 27,
            "2": 28, "3": 29,
            "4": 30, "5": 31,
            "6": 32, "7": 33,
            "8": 34, "9": 35
        }


    def hack_shift(self, ciphertext: str):
        ciphertext = ciphertext.upper()
        for key in range(0, 36):
            decoded = ''
            for character in ciphertext:
                if character not in self.english_alphabet_map_extended:
                    continue

                # convert character to its numeric representation
                character_numeric = self.english_alphabet_map_extended[character]

                # subtract current key to numeric representation
                decoded_numerical = (character_numeric - key) % 36

                # transform decoded numeric into str 
                decoded_character, = [k for k, v in self.english_alphabet_map_extended.items() if v == decoded_numerical] 

                decoded += decoded_character
            
            print(f'Key = {key}, plaintext = {decoded}')

def main():
    A1 = Assignment1()

    user_input = input('Enter a ciphertext: ')

    print('Results:')

    A1.hack_shift(user_input)

if __name__ == '__main__':
    main()
    
class Assignment1:

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


    # key = K
    def decryption(self, key: int, ciphertext: str) -> str:
        decoded : str = ''
        for character in ciphertext:
            # numerical representation of the character
            encoded_numerical = self.english_alphabet_map[character]

            # numerical representation of the decoded character
            decoded_numerical = (encoded_numerical - key) % 26

            # transform decoded numerical into decoded character and add to final decoded text
            
            # corresponding character to decoded_numerical
            decoded_character, = [k for k, v in self.english_alphabet_map.items() if v == decoded_numerical]

            decoded += decoded_character
        
        return decoded

def main():
    user_input = input('Enter the ciphertext: ')
    k = int(input('Enter a corresponsing k (key value -> numerical < 26): '))

    decrypter = Assignment1()
        
    decoded = decrypter.decryption(k, user_input.upper())

    print(f'The decoded string is: {decoded}')
    

if __name__ == '__main__':
    main()
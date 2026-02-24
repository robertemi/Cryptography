import numpy as np

class Assignment3_2:
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


    # helper function used to compute the inverse of the key modulo 26
    def inverse_mod_26(self, key):
        a, b = key[0]
        c, d = key[1]
        det = (a*d - b*c) % 26

        # modular inverse of determinant modulo 26
        det_inv = pow(det, -1, 26)

        adj = np.array([[d, -b],
                        [-c, a]], dtype=int)

        return (det_inv * adj) % 26
    
    
    def decryption(self, ciphertext: str = 'xiyj', key = [[11, 8], [3, 7]]) -> str:
        decoded: str = ''

        # key is of dimension 2 x 2 => split ciphertext into 2 groups of length 2
        group1 = 'xi'
        group2 = 'yj'

        groups = [group1.upper(), group2.upper()]

        for group in groups:
            encoded_ch1 = group[0]
            encoded_ch2 = group[1]

            # numerical representation of each encoded character
            encoded_ch1_numerical = self.english_alphabet_map[encoded_ch1]
            encoded_ch2_numerical = self.english_alphabet_map[encoded_ch2]

            # get inverse modulo 26 of the key
            inverse_key = self.inverse_mod_26(key)

            # numerical representation of decoded characters 
            decoded_numerical = np.matmul((encoded_ch1_numerical, encoded_ch2_numerical), inverse_key) % 26

            # transform decoded numerical into decoded (i.e. as string)
            # cast to int to avoid possible errors
            decoded_ch1_numerical = int(decoded_numerical[0])
            decoded_ch2_numerical = int(decoded_numerical[1])

            ch1_decoded_character, = [k for k, v in self.english_alphabet_map.items() if v == decoded_ch1_numerical]
            ch2_decoded_character, = [k for k, v in self.english_alphabet_map.items() if v == decoded_ch2_numerical]

            decoded_group = ch1_decoded_character + ch2_decoded_character

            decoded += decoded_group
        
        return decoded

def main():
    decrypter = Assignment3_2()
    print(f'The decoding of xiyj is: {decrypter.decryption()}')


if __name__ == '__main__':
    main()
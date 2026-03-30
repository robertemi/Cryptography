import pandas as pd


class DES:
    def __init__(self):
        self.key = '3b3898371520f75e'

        row_labels = ["00", "01", "10", "11"]
        col_labels = [format(i, "04b") for i in range(16)]

        self.initial_permutation = [[58, 50, 42, 34, 26, 18, 10, 2],
                                    [60, 52, 44, 36, 28, 20, 12, 4],
                                    [62, 54, 46, 38, 30, 22, 14, 6],
                                    [64, 56, 48, 40, 32, 24, 16, 8],
                                    [57, 49, 41, 33, 25, 17, 9, 1],
                                    [59, 51, 43, 35, 27, 19, 11, 3],
                                    [61, 53, 45, 37, 29, 21, 13, 5],
                                    [63, 55, 47, 39, 31, 23, 15, 7]]

        self.inverse_permutation = [[40, 8, 48, 16, 56, 24, 64, 32],
                                    [39, 7, 47, 15, 55, 23, 63, 31],
                                    [38, 6, 46, 14, 54, 22, 62, 30],
                                    [37, 5, 45, 13, 53, 21, 61, 29],
                                    [36, 4, 44, 12, 52, 20, 60, 28],
                                    [35, 3, 43, 11, 51, 19, 59, 27],
                                    [34, 2, 42, 10, 50, 18, 58, 26],
                                    [33, 1, 41, 9, 49, 17, 57, 25]]

        self.expansion_function = [[32, 1, 2, 3, 4, 5],
                                   [4, 5, 6, 7, 8, 9],
                                   [8, 9, 10, 11, 12, 13],
                                   [12, 13, 14, 15, 16, 17],
                                   [16, 17, 18, 19, 20, 21],
                                   [20, 21, 22, 23, 24, 25],
                                   [24, 25, 26, 27, 28, 29],
                                   [28, 29, 30, 31, 32, 1]]

        self.permutation = [[16, 7, 20, 21],
                            [29, 12, 28, 17],
                            [1, 15, 23, 26],
                            [5, 18, 31, 10],
                            [2, 8, 24, 14],
                            [32, 27, 3, 9],
                            [19, 13, 30, 6],
                            [22, 11, 4, 25]]

        self.pc1 = [[57, 49, 41, 33, 25, 17, 9],
                    [1, 58, 50, 42, 34, 26, 18],
                    [10, 2, 59, 51, 43, 35, 27],
                    [19, 11, 3, 60, 52, 44, 36],
                    [63, 55, 47, 39, 31, 23, 15],
                    [7, 62, 54, 46, 38, 30, 22],
                    [14, 6, 61, 53, 45, 37, 29],
                    [21, 13, 5, 28, 20, 12, 4]]

        self.pc2 = [[14, 17, 11, 24, 1, 5],
                    [3, 28, 15, 6, 21, 10],
                    [23, 19, 12, 4, 26, 8],
                    [16, 7, 27, 20, 13, 2],
                    [41, 52, 31, 37, 47, 55],
                    [30, 40, 51, 45, 33, 48],
                    [44, 49, 39, 56, 34, 53],
                    [46, 42, 50, 36, 29, 32]]

        self.shifts_dict = {1: 1,
                            2: 1,
                            3: 2,
                            4: 2,
                            5: 2,
                            6: 2,
                            7: 2,
                            8: 2,
                            9: 1,
                            10: 2,
                            11: 2,
                            12: 2,
                            13: 2,
                            14: 2,
                            15: 2,
                            16: 1}

        self.s_boxes = {
            "S1": pd.DataFrame([
                [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
            ], index=row_labels, columns=col_labels),

            "S2": pd.DataFrame([
                [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
            ], index=row_labels, columns=col_labels),

            "S3": pd.DataFrame([
                [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
            ], index=row_labels, columns=col_labels),

            "S4": pd.DataFrame([
                [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
            ], index=row_labels, columns=col_labels),

            "S5": pd.DataFrame([
                [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
            ], index=row_labels, columns=col_labels),

            "S6": pd.DataFrame([
                [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
            ], index=row_labels, columns=col_labels),

            "S7": pd.DataFrame([
                [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
            ], index=row_labels, columns=col_labels),

            "S8": pd.DataFrame([
                [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
            ], index=row_labels, columns=col_labels)
        }

        self.round_keys = self.generate_all_round_keys()

    def convert_to_bits(self, string):
        return ''.join(f"{x:08b}" for x in string.encode("utf-8"))

    def bits_to_string(self, bits):
        return ''.join(chr(int(bits[i:i + 8], 2)) for i in range(0, len(bits), 8))

    def circular_shift_left(self, bits, shift):
        shift %= len(bits)
        return bits[shift:] + bits[:shift]

    def xor_bits(self, a, b):
        return ''.join('1' if x != y else '0' for x, y in zip(a, b))

    def pad_plaintext(self, plaintext):
        padding_length = 8 - (len(plaintext) % 8)
        if padding_length == 0:
            padding_length = 8
        return plaintext + chr(padding_length) * padding_length

    def generate_all_round_keys(self):
        key_in_bits = format(int(self.key, 16), '064b')

        key_56_bit = ['0'] * 56
        k = 0
        for i in self.pc1:
            for j in i:
                key_56_bit[k] = key_in_bits[j - 1]
                k += 1

        c = ''.join(key_56_bit[0:28])
        d = ''.join(key_56_bit[28:])

        round_keys = {}

        for iteration_number in range(1, 17):
            shift_amount = self.shifts_dict[iteration_number]
            c = self.circular_shift_left(c, shift_amount)
            d = self.circular_shift_left(d, shift_amount)

            concat_c_d = c + d

            new_key = ['0'] * 48
            k = 0
            for i in self.pc2:
                for j in i:
                    new_key[k] = concat_c_d[j - 1]
                    k += 1

            round_keys[iteration_number] = ''.join(new_key)

        return round_keys

    # iteration number = round of DES
    def key_expansion(self, iteration_number):
        return self.round_keys[iteration_number]

    def encrypt_block(self, plaintext: str, print_rounds=True, block_label=None):
        if len(plaintext) != 8:
            raise ValueError("plaintext block must be exactly 8 characters")

        if block_label is not None:
            print(f"\nBlock {block_label}: {repr(plaintext)}")

        plaintext_in_bits = self.convert_to_bits(plaintext)
        permuted_plaintext = ['0'] * 64

        # IP
        k = 0
        for i in self.initial_permutation:
            for j in i:
                permuted_plaintext[k] = plaintext_in_bits[j - 1]
                k += 1

        permuted_plaintext = ''.join(permuted_plaintext)

        l = permuted_plaintext[0:32]
        r = permuted_plaintext[32:]

        for des_round in range(1, 17):
            old_l = l
            old_r = r

            expanded_r = ['0'] * 48
            k = 0
            for i in self.expansion_function:
                for j in i:
                    expanded_r[k] = old_r[j - 1]
                    k += 1

            expanded_r = ''.join(expanded_r)
            round_key = self.key_expansion(des_round)
            xored_r = self.xor_bits(round_key, expanded_r)

            s_box_result = ''
            s_box_counter = 1

            for i in range(0, len(xored_r), 6):
                current = xored_r[i:i + 6]

                first = current[0]
                last = current[-1]
                first_last_lookup = first + last

                middle = current[1:-1]
                middle_lookup = middle

                current_sbox = 'S' + str(s_box_counter)
                value = self.s_boxes[current_sbox].loc[first_last_lookup, middle_lookup]

                s_box_result += format(value, '04b')
                s_box_counter += 1

            permuted_sbox_result = ['0'] * 32
            k = 0
            for i in self.permutation:
                for j in i:
                    permuted_sbox_result[k] = s_box_result[j - 1]
                    k += 1

            permuted_sbox_result = ''.join(permuted_sbox_result)

            l = old_r
            new_r = self.xor_bits(old_l, permuted_sbox_result)
            r = new_r

            if print_rounds:
                round_output = l + r
                print(f"Round: {des_round}, output: {round_output}, key: {round_key}")

        final_block = r + l

        ciphertext_bits = ['0'] * 64
        k = 0
        for i in self.inverse_permutation:
            for j in i:
                ciphertext_bits[k] = final_block[j - 1]
                k += 1

        ciphertext_bits = ''.join(ciphertext_bits)
        ciphertext_hex = format(int(ciphertext_bits, 2), '016x')

        if print_rounds:
            print(f"Ciphertext: {ciphertext_bits} ({ciphertext_hex})")

        return ciphertext_hex

    def encrypt(self, plaintext: str, print_rounds=True):
        plaintext = self.pad_plaintext(plaintext)

        ciphertext_blocks = []

        for block_number, i in enumerate(range(0, len(plaintext), 8), start=1):
            current_block = plaintext[i:i + 8]
            current_ciphertext_hex = self.encrypt_block(
                current_block,
                print_rounds=print_rounds,
                block_label=block_number
            )
            ciphertext_blocks.append(current_ciphertext_hex)

        return ''.join(ciphertext_blocks)
    

    def encrypt_cbc(self, plaintext: str, iv: str, print_rounds=True):
        if len(iv) != 8:
            raise ValueError("iv must be exactly 8 characters")

        plaintext = self.pad_plaintext(plaintext)
        ciphertext_blocks = []

        previous_ciphertext_bits = self.convert_to_bits(iv)

        for block_number, i in enumerate(range(0, len(plaintext), 8), start=1):
            current_block = plaintext[i:i + 8]
            current_block_bits = self.convert_to_bits(current_block)

            xored_block_bits = self.xor_bits(current_block_bits, previous_ciphertext_bits)
            xored_block_string = self.bits_to_string(xored_block_bits)

            print(f"\nCBC Block {block_number}: {repr(current_block)}")
            print(f"XOR input: {xored_block_bits}")

            current_ciphertext_hex = self.encrypt_block(
                xored_block_string,
                print_rounds=print_rounds,
                block_label=f"{block_number} (after CBC XOR)"
            )

            ciphertext_blocks.append(current_ciphertext_hex)
            previous_ciphertext_bits = format(int(current_ciphertext_hex, 16), '064b')

        return ''.join(ciphertext_blocks)


if __name__ == "__main__":
    des = DES()

    plaintext = "DES algoritm is better than classical algorithms"
    # needed for CBC 
    iv = "12345678"

    print("=== ECB ===")
    ciphertext_ecb = des.encrypt(plaintext, print_rounds=True)
    print("\nFinal ECB ciphertext (hex):", ciphertext_ecb)

    print("\n=== CBC ===")
    ciphertext_cbc = des.encrypt_cbc(plaintext, iv, print_rounds=True)
    print("\nFinal CBC ciphertext (hex):", ciphertext_cbc)
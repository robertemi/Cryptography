# a)

# 2 ** n levels of signal, where n = number of bits
def signal_to_bits(n: int) -> int:
    return 2 ** n


# b)

class Assignment3:
    def __init__(self, message):
        self.message = message.upper()

        self.alphabet_map = {
            "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
            "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
            "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
            "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
            "Z": 25
        }

    def encode_5bit(self):
        binary_codes = []
        voltages = []

        V0 = 1  # max amplitude
        step = 2 * V0 / 31  # quantization step

        for ch in self.message:           
            if ch not in self.alphabet_map:
                continue

            value = self.alphabet_map[ch]

            # binary representation
            binary = format(value, "05b")
            binary_codes.append(binary)

            # voltage in range [-V0, V0]
            voltage = -V0 + value * step
            voltages.append(voltage)

        return binary_codes, voltages


def main():
    message = "codebyjava"

    # part a
    print("Part a:")
    print("3-bit A/D converter levels =", signal_to_bits(3))

    # part b
    solver = Assignment3(message)
    binaries, voltages = solver.encode_5bit()

    print("\nBinary representation (5-bit) of codebyjava:")
    print(" ".join(binaries))

    print("\nAnalog signal values (Volts):")
    for character, binary, volt in zip(message.upper(), binaries, voltages):
        print(f"{character} -> binary={binary}, voltage={volt:.4f} V")


if __name__ == "__main__":
    main()
import math
from collections import Counter


class Assignment2:
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

        self.common_letters = ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D"]
        self.top_digrams = ["TH", "HE", "IN", "ER", "AN", "RE", "ON", "AT", "EN", "ND"]
        self.top_trigrams = ["THE", "AND", "ING", "HER", "ERE", "ENT", "THA", "NTH", "WAS", "ETH"]

    def mod_inverse(self, x: int, mod: int) -> int | None:
        if math.gcd(x, mod) != 1:
            return None
        return pow(x, -1, mod)

    def decrypt_affine(self, ciphertext: str, a: int, b: int) -> str:
        a_inverse = self.mod_inverse(a, 26)
        if a_inverse is None:
            return ""

        decoded = ""
        ciphertext = ciphertext.upper()

        for ch in ciphertext:
            if ch not in self.english_alphabet_map:
                continue

            y = self.english_alphabet_map[ch]
            x = (a_inverse * (y - b)) % 26

            decoded_character, = [
                k for k, v in self.english_alphabet_map.items()
                if v == x
            ]

            decoded += decoded_character

        return decoded

    def score_text(self, text: str) -> float:
        english_freq = {
            "A": 8.17, "B": 1.49, "C": 2.78, "D": 4.25, "E": 12.70,
            "F": 2.23, "G": 2.02, "H": 6.09, "I": 6.97, "J": 0.15,
            "K": 0.77, "L": 4.03, "M": 2.41, "N": 6.75, "O": 7.51,
            "P": 1.93, "Q": 0.10, "R": 5.99, "S": 6.33, "T": 9.06,
            "U": 2.76, "V": 0.98, "W": 2.36, "X": 0.15, "Y": 1.97,
            "Z": 0.07
        }

        if len(text) == 0:
            return float("-inf")

        text = "".join(ch for ch in text if ch in self.english_alphabet_map)
        n = len(text)

        # chi-squared score: lower is better
        chi_squared = 0.0
        for letter in self.english_alphabet_map:
            observed = text.count(letter)
            expected = english_freq[letter] * n / 100

            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected

        # extra bonuses for common patterns
        bonus = 0
        common_words = ["THE", "AND", "ING", "ION", "ENT", "TH", "HE", "IN", "ER", "AN", "IT", "IS"]
        for pattern in common_words:
            bonus += text.count(pattern) * 2

        # higher score should be better
        return -chi_squared + bonus

    def solve_key_from_pairs(self, plain1: str, cipher1: str, plain2: str, cipher2: str):
        x1 = self.english_alphabet_map[plain1]
        x2 = self.english_alphabet_map[plain2]
        y1 = self.english_alphabet_map[cipher1]
        y2 = self.english_alphabet_map[cipher2]

        # a(x1 - x2) ≡ (y1 - y2) mod 26
        delta_x = (x1 - x2) % 26
        delta_y = (y1 - y2) % 26

        delta_x_inverse = self.mod_inverse(delta_x, 26)
        if delta_x_inverse is None:
            return None

        a = (delta_y * delta_x_inverse) % 26
        if math.gcd(a, 26) != 1:
            return None

        b = (y1 - a * x1) % 26
        return a, b

    def hack_affine_frequency(self, ciphertext: str):
        ciphertext = "".join(
            ch for ch in ciphertext.upper()
            if ch in self.english_alphabet_map
        )

        freq = Counter(ciphertext)
        most_common_cipher_letters = [ch for ch, _ in freq.most_common(6)]

        candidates = []

        for i in range(len(most_common_cipher_letters)):
            for j in range(len(most_common_cipher_letters)):
                if i == j:
                    continue

                cipher1 = most_common_cipher_letters[i]
                cipher2 = most_common_cipher_letters[j]

                # try mapping frequent ciphertext letters to frequent English letters
                for plain1 in self.common_letters[:6]:
                    for plain2 in self.common_letters[:6]:
                        if plain1 == plain2:
                            continue

                        key = self.solve_key_from_pairs(plain1, cipher1, plain2, cipher2)
                        if key is None:
                            continue

                        a, b = key
                        plaintext = self.decrypt_affine(ciphertext, a, b)
                        score = self.score_text(plaintext)

                        candidates.append((score, a, b, plaintext, plain1, cipher1, plain2, cipher2))

        if not candidates:
            return None

        candidates.sort(reverse=True, key=lambda item: item[0])
        return candidates


def main():
    solver = Assignment2()
    ciphertext = input("Enter ciphertext: ")

 
    candidates = solver.hack_affine_frequency(ciphertext)

    if candidates is None:
        print("No valid key candidates found.")
        return

    best_score, a, b, plaintext, plain1, cipher1, plain2, cipher2 = candidates[0]

    print("\nBest result:")
    print(f"Plaintext = {plaintext}")
    print(f"a = {a}, b = {b}")
    print(f"Derived from guesses: {cipher1}->{plain1}, {cipher2}->{plain2}")
    print(f"Score = {best_score}")

    print("\nTop 5 candidates:")
    for score, a, b, plaintext, plain1, cipher1, plain2, cipher2 in candidates[:15]:
        print(
            f"score={score}, a={a}, b={b}, "
            f"guesses {cipher1}->{plain1}, {cipher2}->{plain2}, "
            f"plaintext={plaintext}"
        )


if __name__ == "__main__":
    main()
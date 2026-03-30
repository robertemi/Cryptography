'''

GF(2^4) irreductible polynomial = X^4 + X + 1 -> in hex: 0x13
GF(2^8) irreductible polynomial = X^8 + X^4 + X^3 + X + 1 -> in hex: 0x11B


'''

def gf_reduce(x, mod_poly, degree):
    """Reduce polynomial x modulo mod_poly."""
    while x.bit_length() - 1 >= degree:
        shift = (x.bit_length() - 1) - degree
        x ^= mod_poly << shift
    return x

def gf_mul(a, b, mod_poly, degree):
    """Multiply in GF(2^m) modulo mod_poly."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= mod_poly
    return gf_reduce(result, mod_poly, degree)


A = 0x73
B = 0x4E
C = 0x85

# in GF(2^4)
mod4 = 0x13   # x^4 + x + 1
deg4 = 4

sum_ab_4 = A ^ B
D4 = gf_mul(sum_ab_4, C, mod4, deg4)

print("GF(2^4):")
print(f"A + B = 0x{sum_ab_4:02X}")
print(f"D = (A+B)*C = 0x{D4:02X}")

# in GF(2^8)
mod8 = 0x11B  # x^8 + x^4 + x^3 + x + 1
deg8 = 8

sum_ab_8 = A ^ B
D8 = gf_mul(sum_ab_8, C, mod8, deg8)

print("\nGF(2^8):")
print(f"A + B = 0x{sum_ab_8:02X}")
print(f"D = (A+B)*C = 0x{D8:02X}")
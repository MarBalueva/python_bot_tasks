def main(x):
    A = x & 0b111111
    B = (x >> 6) & 0b111
    C = (x >> 9) & 0b11111
    D = (x >> 14) & 0b111111111111111
    E = (x >> 29) & 0b1
    F = (x >> 30) & 0b1
    G = (x >> 31) & 0b1
    result = 0
    result |= B << 29
    result |= C << 24
    result |= D << 9
    result |= A << 3
    result |= E << 2
    result |= G << 1
    result |= F
    return result

print(hex(main(0xbd4bcd5b))) #0xa6ea5ede
print(hex(main(0x0de54045))) #0x206f2a28
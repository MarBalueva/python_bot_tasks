def main(n, a, b):
    result = 0
    for i in range(1, b + 1):
        current_out = 0
        for k in range(1, a + 1):
            current_in = 0
            for j in range(1, n + 1):
                current_in += 1 - i - 75 * (13 + 64 * j ** 3 + k ** 2) ** 5
            current_out += current_in
        result += current_out
    return result


print('%.2e' % main(7, 5, 7))
print('%.2e' % main(5, 7, 6))

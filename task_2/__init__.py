def main(x):
    if x < 38:
        return 6 - x ** 2 + x ** 7
    if 38 <= x < 101:
        return x ** 6
    if x >= 101:
        return (60 - 28 * x ** 3 - 25 * x) ** 7 - \
               (x ** 3 / 49) ** 2


print('%.2e' % main(-23))
print('%.2e' % main(127))

def main(n):
    if n == 0:
        return 0.68
    if n == 1:
        return 0.99
    if n >= 2:
        return 0.01 + main(n - 1) ** 2 + main(n - 2) ** 3 / 75


print('%.2e' % main(6))
print('%.2e' % main(2))
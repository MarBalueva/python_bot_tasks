import math


def main(y, x):
    result = 0
    n = len(y)
    for i in range(1, n + 1):
        result += (92 * y[n - i] - x[math.trunc(n - i / 3)] ** 2 -
                   y[n - i] ** 3) ** 5
    return result


print('%.2e' % main([0.57, -0.34, -0.87, 0.26, 0.35, -0.95],
                    [-0.16, -0.31, -0.57, 0.69, -0.88, -0.02]))
print('%.2e' % main([0.72, -0.0, 0.28, 0.19, -0.86, 0.31],
                    [-0.95, 0.37, -0.77, -0.28, 0.35, -0.57]))

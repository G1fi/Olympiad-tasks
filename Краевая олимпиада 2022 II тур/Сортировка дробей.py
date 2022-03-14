# Дудко Павел Иванович

import sys
import math


def main():
    n, q = map(int, sys.stdin.readline().split())
    a = tuple(map(int, sys.stdin.readline().split()))
    b = tuple(map(int, sys.stdin.readline().split()))
    c = tuple(map(int, sys.stdin.readline().split()))

    drobs = []

    for ind_a, i in enumerate(a):
        for ind_b, j in enumerate(b):
            drobs.append((ind_a, ind_b, i/j))

    drobs = sorted(drobs, key=lambda drob: drob[2])

    for i in c:
        drob_i = drobs[i-1]
        a_i = a[drob_i[0]]
        b_i = b[drob_i[1]]
        gcd = math.gcd(a_i, b_i)
        if gcd != 1:
            a_i = int(a_i / gcd)
            b_i = int(b_i / gcd)

        print(a_i, b_i)

    #     index_a = (i - 1) // n
    #     index_b = (i - 1) % n
    #
    #     print(a[index_a], b[index_b])


if __name__ == '__main__':
    main()

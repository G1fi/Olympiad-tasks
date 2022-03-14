# Дудко Павел Иванович

import sys


def main():
    t = int(sys.stdin.readline())

    for i in range(t):
        n, a, b = map(int, sys.stdin.readline().split())
        if a > b:
            a, b = b, a

        summa = a + b
        answ = 0

        for j in range(1, summa // n + 1):
            count = j * n

            if count == summa:
                answ += 1
                continue

            else:
                offset = 0

                if a < count:
                    offset += count - a

                if b < count:
                    offset += count - b

                answ += count - offset + 1

        print(answ)


if __name__ == '__main__':
    main()

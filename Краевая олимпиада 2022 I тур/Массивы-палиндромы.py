# Дудко Павел Иванович

import sys
import math

def is_palindrom(target_list):
    dlina = len(target_list)
    if dlina % 2 == 1:
        dlina -= 1
    dlina = int(dlina / 2)

    for i in range(dlina):
        if target_list[i] != target_list[-i - 1]:
            return False

    return True


def main():
    n, m = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    k = 0

    if n < m:
        k = n
    if m < n:
        k = m

    a_targ = n - k

    for count in range(a_targ, n+1):
        for a_nach in range(0, count+1):
            a_con = -(count - a_nach)
            if a_con == 0:
                a_new = A[a_nach:]
            else:
                a_new = A[a_nach:a_con]
            if is_palindrom(a_new):
                print(len(a_new))
                exit()


if __name__ == '__main__':
    main()

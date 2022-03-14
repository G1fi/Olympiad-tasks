# Дудко Павел Иванович

import sys


def main():
    n = int(sys.stdin.readline())
    f = int(sys.stdin.readline())
    if f == 1:
        d = list(map(int, sys.stdin.readline().split()))
    if f == 2:
        m, x, y, z = list(map(int, sys.stdin.readline().split()))
        inp_list2 = list(map(int, sys.stdin.readline().split()))
        d = []
        d.extend(inp_list2)
        for i in range(m + 1, n + 1):
            d.append((x * d[i-3] + y * d[i-2] + z) % (10**9) + 1)


    end_point = max(d)
    ind_end_point = d.index(end_point)
    max_value = 0

    for max_value in range(end_point, 9999999999):
        flag = True

        for j in range(ind_end_point - 1, -(n - ind_end_point), -1):
            max_value -= 1
            if max_value < d[j]:
                flag = False
                break

        if flag is False:
            continue

        answ = ind_end_point+2
        if answ > n:
            answ -= n

        print(max_value, answ)
        break



if __name__ == '__main__':
    main()

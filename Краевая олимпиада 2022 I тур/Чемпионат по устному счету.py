# Дудко Павел Иванович

import sys


def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    q = int(sys.stdin.readline())
    summa = sum(nums)
    offset = 0

    for i in range(q):
        command = list(map(int, sys.stdin.readline().split()))

        if command[0] == 1:
            index = command[1] - 1 - offset

            if index < -n:
                index = -(-index % n)

            summa = summa - nums[index] + command[2]
            nums[index] = command[2]

        if command[0] == 2:
            offset += command[1]

        print(summa)


if __name__ == '__main__':
    main()

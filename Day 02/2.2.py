#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().strip().split('\n')
    input_list = [list(map(int, i.split())) for i in content]

    sum_divisible = 0
    for row in input_list:
        sum_divisible += check_row(row)
    print(sum_divisible)


def check_row(row):
    for n in row:
        for m in row:
            if n > m and n % m == 0:
                return n // m


if __name__ == '__main__':
    main()
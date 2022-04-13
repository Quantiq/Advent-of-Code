#!/usr/bin/env python3

import sys

def main():
    n = int(sys.argv[1])
    spiral = {(0, 0): 1}
    x, y, count = 0, 0, 1

    while True:

        # right
        for i in range(count):
            x += 1
            check_iter(spiral, n, x, y)

        # up
        for i in range(count):
            y += 1
            check_iter(spiral, n, x, y)

        # left
        for i in range(count + 1):
            x -= 1
            check_iter(spiral, n, x, y)

        # down
        for i in range(count + 1):
            y -= 1
            check_iter(spiral, n, x, y)

        count += 2


def check_iter(spiral, puzzle_input, x, y):
    index_sum = get_surrounding_sum(spiral, x, y)
    if index_sum > puzzle_input:
        print(index_sum)
        exit()
    else:
        spiral[x, y] = index_sum


def get_surrounding_sum(spiral, x, y):
    index_sum = 0
    for a in range(x - 1, x + 2):
        for b in range(y - 1, y + 2):
            if (a, b) in spiral:
                index_sum += spiral[a, b]
    return index_sum


if __name__ == '__main__':
    main()
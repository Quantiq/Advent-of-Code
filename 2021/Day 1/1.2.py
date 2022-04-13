#!/usr/bin/env python3


def main():

    sums = []
    increased_count = 0

    with open("input.txt") as f:
        content = [int(i) for i in f.read().splitlines()]

    for i in range(len(content) - 2):
        x, y, z = content[i], content[i+1], content[i+2]
        sums.append(x + y + z)

    for i in range(len(sums) - 1):
        if sums[i+1] > sums[i]:
            increased_count += 1

    print(increased_count)

if __name__ == '__main__':
    main()
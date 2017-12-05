#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        jumps = [int(i) for i in f.read().splitlines()]
    i, step_count = 0, 0

    while i in range(0, len(jumps)):
        temp = i    # store i in temp value
        i += jumps[i]
        jumps[temp] += 1
        step_count += 1
    print(step_count)


if __name__ == '__main__':
    main()
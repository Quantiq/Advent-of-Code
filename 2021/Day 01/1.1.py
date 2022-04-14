#!/usr/bin/env python3

def main():

    increased_count = 0

    with open("input.txt") as f:
        content = [int(i) for i in f.read().splitlines()]

    for i in range(len(content) - 1):
        x = content[i]
        y = content[i+1]
        if y > x:
            increased_count += 1

    print(increased_count)

if __name__ == '__main__':
    main()
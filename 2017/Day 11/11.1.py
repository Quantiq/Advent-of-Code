#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().strip().split(',')

        x, y, z = 0, 0, 0

        for i in content:
            if i == 'n':
                y += 1
                z -= 1
            elif i == 'ne':
                x += 1
                z -= 1
            elif i == 'nw':
                x -= 1
                y += 1
            elif i == 's':
                y -= 1
                z += 1
            elif i == 'se':
                x += 1
                y -= 1
            elif i == 'sw':
                x -= 1
                z += 1

        print((abs(x) + abs(y) + abs(z)) // 2)


if __name__ == '__main__':
    main()
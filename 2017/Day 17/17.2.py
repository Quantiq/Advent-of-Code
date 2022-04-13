#!/usr/bin/env python3

def main():
    pos, step_count, insertions = 0, 359, 50000000

    for i in range(1, insertions + 1):
        pos = (pos + step_count) % i
        if pos == 0:
            cur = i
        pos += 1

    print(cur)


if __name__ == '__main__':
    main()
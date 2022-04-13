#!/usr/bin/env python3

def main():
    pos, step_count, insertions = 0, 359, 2017

    spinlock = [0]

    for i in range(1, insertions + 1):
        pos = (pos + step_count) % i
        spinlock.insert(pos + 1, i)
        pos += 1
    
    print(spinlock[pos + 1])


if __name__ == '__main__':
    main()
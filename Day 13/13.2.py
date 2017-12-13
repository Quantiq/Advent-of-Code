#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().splitlines()

    firewall, delay = {}, 0

    for i in content:
        a = i.partition(": ")
        firewall[int(a[0])] = int(a[2])

    while True:
        for depth, f_range in firewall.items():
            tick_size = 2 * (f_range - 1)
            if (depth + delay) % tick_size == 0:
                delay += 1
                break
        else:
            break
    print(delay)


if __name__ == '__main__':
    main()
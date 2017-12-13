#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().splitlines()

    firewall, severity = {}, 0

    for lines in content:
        a = lines.partition(": ")
        firewall[int(a[0])] = int(a[2])

    for depth, f_range in firewall.items():
        tick_size = 2 * (f_range - 1)
        if depth % tick_size == 0:
            severity += depth * f_range
    print(severity)


if __name__ == '__main__':
    main()
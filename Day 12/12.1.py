#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = [i.split() for i in f.read().strip().splitlines()]

    pipes = {}

    for line in content:
        key = int(line[0])
        vals = [int(i.strip(',')) for i in line[2:]]
        pipes[key] = tuple(vals)

    count = 0
    seen, prev = [0], []

    while set(seen) != set(prev):
        for i in seen:
            for n in pipes[i]:
                if n not in seen:
                    seen.append(n)
            prev = seen

    print(len(seen))


if __name__ == '__main__':
    main()
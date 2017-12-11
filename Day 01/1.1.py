#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = [int(i) for i in f.read().strip()]

    total = 0

    for index, i in enumerate(content):
        if index + 1 < len(content):
            if i == content[index + 1]:
                total += i
        else:
            if i == content[0]:
                total += i
    print(total)


if __name__ == '__main__':
    main()
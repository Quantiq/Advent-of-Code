#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = list(f.read())

    total = 0

    for index, i in enumerate(content):
        if index + 1 < len(content):
            if int(i) == int(content[index + 1]):
                total += int(i)
        else:
            if int(i) == int(content[0]):
                total += int(i)
    print(total)


if __name__ == '__main__':
    main()
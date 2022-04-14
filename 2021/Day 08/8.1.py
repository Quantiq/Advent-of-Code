#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        output_list = [i.split(" | ")[-1].split() for i in f.read().splitlines()]

    count = 0

    for line in output_list:
        for string in line:
            if len(string) in (2, 3, 4, 7):
                count += 1

    print(count)


if __name__ == "__main__":
    main()
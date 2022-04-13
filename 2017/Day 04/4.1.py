#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
            content = f.read().splitlines()
    input_list = [list(i.split()) for i in content]
    valid = 0

    for passphrase in input_list:
        if is_valid(passphrase):
            valid += 1
    print(valid)


def is_valid(passphrase):
    for index, word in enumerate(passphrase):
        for i in range(index + 1, len(passphrase)):
            if word == passphrase[i]:
                return False
    return True


if __name__ == '__main__':
    main()
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
            if is_anagram(word, passphrase[i]):
                return False
    return True


def is_anagram(word_a, word_b):
    if len(word_a) != len(word_b):
        return False
    else:
        word_a, word_b = list(word_a), list(word_b)
        word_a.sort(), word_b.sort()
        return word_a == word_b


if __name__ == '__main__':
    main()
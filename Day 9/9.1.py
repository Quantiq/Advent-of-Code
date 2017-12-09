#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        stream = list(f.read())

    valid_characters = ['{', '}']
    ignore, score, m = False, 0, 0

    for index, char in enumerate(stream):
        if char == '<' and isnt_not(index, stream):
            ignore = True

        if not ignore and char in valid_characters:
            if char == '{':
                m += 1
                score += m
            elif char == '}':
                m -= 1

        if char == '>' and isnt_not(index, stream):
            ignore = False

    print(score)


def isnt_not(index, stream):
    '''Check if the previous characters cancel the current character'''
    if stream[index - 1] != '!':
        return True
    else:
        i = 0
        while stream[(index - 1) - i] == '!':
            i += 1
        return i % 2 == 0


if __name__ == '__main__':
    main()
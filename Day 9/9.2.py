def main():
    with open("input.txt") as f:
        stream = list(f.read())

    ignore, count = True, 0

    for index, char in enumerate(stream):
        if char == '>' and isnt_not(index, stream):
            ignore = True

        if not ignore and char != '!' and isnt_not(index, stream):
            count += 1

        if char == '<' and isnt_not(index, stream):
            ignore = False

    print(count)


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
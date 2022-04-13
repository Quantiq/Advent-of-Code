

def main():
    with open("input.txt") as f:
        content = [i.replace(",", "").split() for i in f.read().splitlines()]

    stack = []

    for lines in content:
        stack.append([i for i in lines if i.isalpha()])

    key_a = stack[0][0]

    for x in range(5):
        key_b = key_a
        for i in stack:
            if key_b in i[1:]:
                key_b = i[0]

        if key_a == key_b:
            print(key_a)
            break
        else:
            key_a = key_b


if __name__ == '__main__':
    main()
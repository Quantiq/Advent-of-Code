def main():
    with open("input.txt") as f:
        content = [i.replace(",", "").replace("(", "").replace(")", "").replace("->", "").split() for i in f.read().splitlines()]

    for x, lines in enumerate(content):
        for y, i in enumerate(lines):
            if i.isdigit():
                content[x][y] = int(i)

    global stack_vals
    global key_vals

    stack_vals, key_vals, new = {}, {}, []

    for i in content:
        stack_vals[i[0]] = i[1]
        if i[2:] != []:
            key_vals[i[0]] = tuple(i[2:])

    for key, key_tuple in key_vals.items():
        stupid_list = []
        for i in key_tuple:
            stupid_list.append(key_sum(i))
        if max(stupid_list) != min(stupid_list):
            print(key_tuple)
            print(stupid_list)
            print(stack_vals[key])
            print("")

def key_sum(key):
    if key not in key_vals:
        return stack_vals[key]
    else:
        n = 0
        for i in key_vals[key]:
            n += key_sum(i)
        return n + stack_vals[key]


if __name__ == '__main__':
    main()
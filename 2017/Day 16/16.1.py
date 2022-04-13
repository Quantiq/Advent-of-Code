#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().strip().split(",")

    moves = parse_input(content)
    programs = "abcdefghijklmnop"

    for move in moves:
        programs = dance(move, programs)
    
    print(programs)


def dance(move, programs):

    programs = list(programs)

    if move[0] == 'spin':
        s = move[1]
        programs = programs[-s:] + programs[:-s]
    elif move[0] == 'exchange':
        a = move[1]
        b = move[2]
        programs[a], programs[b] = programs[b], programs[a]
    elif move[0] == 'partner':
        a = programs.index(move[1])
        b = programs.index(move[2])
        programs[a], programs[b] = programs[b], programs[a]

    return "".join(programs)


def parse_input(content):

    moves = []

    for i in content:
        if i[0] == 'p':
            moves.append(['partner', i[1], i[3]])
        elif i[0] == 's':
            moves.append(['spin', int(i[1:])])
        elif i[0] == 'x':
            a = i.strip('x').split('/')
            moves.append(['exchange', int(a[0]), int(a[1])])

    return moves


if __name__ == '__main__':
    main()
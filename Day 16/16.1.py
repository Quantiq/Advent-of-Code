with open("input.txt") as f:
    content = f.read().strip().split(",")

moves = []
programs = list("abcdefghijklmnop")

# input parsing
for i in content:
    if i[0] == 'p':
        moves.append(['p', i[1], i[3]])
    elif i[0] == 's':
        moves.append(['s', int(i[1:])])
    elif i[0] == 'x':
        tup = i.strip('x').partition('/')
        moves.append(['x', int(tup[0]), int(tup[2])])

iters_list = []
i = 0

iters_list.append("".join(programs))

while True:
    i += 1
    for move in moves:
        # spin
        if move[0] == 's':
            n = move[1]
            programs = programs[-n:] + programs[:-n]
        
        # exchange
        elif move[0] == 'x':
            a = move[1]
            b = move[2]
            programs[a], programs[b] = programs[b], programs[a]
        
        # partner
        elif move[0] == 'p':
            a = programs.index(move[1])
            b = programs.index(move[2])
            programs[a], programs[b] = programs[b], programs[a]

    programs = "".join(programs)

    if programs not in iters_list:
        iters_list.append(programs)
        programs = list(programs)
    else:
        break

print(iters_list[1000000000 % i])
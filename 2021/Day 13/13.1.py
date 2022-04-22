#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        data = [i for i in f.read().splitlines()]

    # seperate coordinates and fold data in seperate lists
    for i, val in enumerate(data):
        if val == '':
            coordinates = data[:i]
            folds = data[i+1:]
    
    coordinates = [[int(j) for j in i.split(',')] for i in coordinates]

    # for each fold, translate coordinates using formula: num - ((num - fold_num)  * 2)
    for fold in folds:
        axis = fold[11]
        fold_num = int(fold[13:])

        if axis == 'y':
            for coordinate in coordinates:
                y = coordinate[1]
                if ((y - fold_num) * 2) >= 0:
                    coordinate[1] = y - ((y - fold_num) * 2)

        if axis == 'x':
            for coordinate in coordinates:
                x = coordinate[0]
                if ((x - fold_num) * 2) >= 0:
                    coordinate[0] = x - ((x - fold_num) * 2)

        break    # only need the first fold

    # return count of coordinates that are not duplicates
    seen = []
    count = 0
    for coordinate in coordinates:
        if coordinate not in seen:
            count += 1
            seen.append(coordinate)

    print(count)


if __name__ == '__main__':
    main()
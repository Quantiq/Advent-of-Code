#!/usr/bin/env python3

import numpy as np

def main():

    with open("input.txt") as f:
        data = np.asarray([[int(i) for i in j] for j in f.read().splitlines()])

    # pad the sides of the array with -1
    data = np.pad(data, 1, constant_values=-1)
    data = np.ndarray.tolist(data)

    basins = find_basins(data)
    product = find_product(basins)

    print(product)


def find_basins(data):
    # find locations where adjacent values are greater or -1

    basins = []

    for y_index, y in enumerate(data[1:-1]):
        for x_index, x in enumerate(y[1:-1]):
            
            y_in = y_index + 1
            x_in = x_index + 1

            if x < data[y_in - 1][x_in] or data[y_in - 1][x_in] == -1:               # check down
                if x < data[y_in + 1][x_in] or data[y_in + 1][x_in] == -1:           # check up
                    if x < data[y_in][x_in - 1] or data[y_in][x_in - 1] == -1:       # check left
                        if x < data[y_in][x_in + 1] or data[y_in][x_in + 1] == -1:   # check right

                            basins.append(flood_fill(data, x_in, y_in, []))
            
            y_in = 0
            x_in = 0

    return basins


def flood_fill(data, x, y, seen):
    # perform a recursive flood fill finding all adjacent values that are not 9 or -1

    if data[y][x] == 9 or data[y][x] == -1:
        return

    if (x, y) not in seen:

        seen.append((x,y))

        flood_fill(data, x - 1, y, seen)
        flood_fill(data, x + 1, y, seen)
        flood_fill(data, x, y - 1, seen)
        flood_fill(data, x, y + 1, seen)

        return len(seen)


def find_product(basins):
    # return the product of the 3 highest basins in the basins list

    return np.prod(sorted(basins, reverse=True)[:3])


if __name__ == "__main__":
    main()
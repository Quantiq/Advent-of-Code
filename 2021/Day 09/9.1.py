#!/usr/bin/env python3

import numpy as np

def main():

    with open("input.txt") as f:
        data = np.asarray([[int(i) for i in j] for j in f.read().splitlines()])

    data = np.pad(data, 1, constant_values=-1)
    data = np.ndarray.tolist(data)

    risk = 0

    for y_index, y in enumerate(data[1:-1]):
        for x_index, x in enumerate(y[1:-1]):
            
            y_in = y_index + 1
            x_in = x_index + 1

            if x < data[y_in - 1][x_in] or data[y_in - 1][x_in] == -1:               # check down
                if x < data[y_in + 1][x_in] or data[y_in + 1][x_in] == -1:           # check up
                    if x < data[y_in][x_in - 1] or data[y_in][x_in - 1] == -1:       # check left
                        if x < data[y_in][x_in + 1] or data[y_in][x_in + 1] == -1:   # check right

                            risk = risk + x + 1
            
            y_in = 0
            x_in = 0

    print(risk)


if __name__ == "__main__":
    main()
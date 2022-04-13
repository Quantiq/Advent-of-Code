#!/usr/bin/env python3

def main():

    data = []
    highest_value = 0

    # write data to list
    with open("input.txt") as f:
        for i in f.read().splitlines():
            i = i.replace(" -> ",",")
            data.append(i.split(","))

    # convert values to integers            
    data = [[int(i) for i in j] for j in data]

    # find highest value
    for row in data:
        for i in row:
            if i > highest_value:
                highest_value = i

    # populate array with 0s
    array = [[0 for x in range(highest_value + 1)] for y in range(highest_value + 1)]

    for i in data:

        # coordinates
        x1 = i[0]
        y1 = i[1]
        x2 = i[2]
        y2 = i[3]

        # vertical line
        if x1 == x2:
            for j in range(abs(y1 - y2) + 1):
                array[min(y1,y2) + j][x1] += 1

        # horizontal line
        if y1 == y2:
            for j in range(abs(x1 - x2) + 1):
                array[y1][min(x1,x2) + j] += 1

        # diagonal line top left to bottom right
        if (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
            for j in range(abs(x1 - x2) + 1):
                array[min(y1,y2) + j][min(x1, x2) + j] += 1

        # diagonal line top right to bottom left
        if (x1 < x2 and y1 > y2) or (x1 > x2 and y1 < y2):
            if x1 < x2:
                for j in range(abs(x1 - x2) + 1):
                    array[y1 - j][x1 + j] += 1
            if x1 > x2:
                for j in range(abs(x1 - x2) + 1):
                    array[y1 + j][x1 - j] += 1

    
    count = 0

    # count instances in array where overlaps >= 2
    for i in array:
        for j in i:
            if j >= 2:
                count += 1

    print(count)

if __name__ == "__main__":
    main()
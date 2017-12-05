#!/usr/bin/env python3

import sys

def main():
    puzzle_input = int(sys.argv[1])
    corners = []
    ring, ring_num, total = 0, 0, 1

    while total < puzzle_input:
        ring_num += 1
        ring += 8
        total += ring

    # Find corners for ring
    for i in range(4):
        corners.append(total - ((ring//4) * i))

    if puzzle_input in corners:
        print(ring_num * 2)
    else:
        corners.append(corners[3] - (ring//4)) # add "hidden" corner
        distance_from_corner = min([abs(puzzle_input - corner) 
                                    for corner in corners])
        print((ring_num * 2) - distance_from_corner)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().strip().split('\n')
    input_list = [list(map(int, i.split())) for i in content]
 
    sum_diff = 0
    for row in input_list:
        sum_diff += (max(row) - min(row))
    print(sum_diff)


if __name__ == '__main__':
    main()
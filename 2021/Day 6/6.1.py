#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        fish_list = [int(i) for i in f.read().split(",")]

    days = 80
    
    for day in range(days):

        for index, fish in enumerate(fish_list):
            
            if fish == 0:
                fish_list.append(9)
                fish_list[index] = 6
            else:
                fish_list[index] -= 1

    print(len(fish_list))


if __name__ == "__main__":
    main()
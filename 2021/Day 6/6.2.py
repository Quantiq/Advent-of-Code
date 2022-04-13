#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    
    for i in data:
        fish[i] += 1
    
    days = 256

    increment = 0
    new_fish = {}


    for day in range(days):

        for fish_key, fish_value in fish.items():

            if fish_key == 0:
                increment = fish_value
            else:
                new_fish[fish_key - 1] = fish_value

        new_fish[6] += increment
        new_fish[8] = increment

        fish = new_fish

    print(sum(fish.values()))


if __name__ == "__main__":
    main()
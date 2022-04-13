#!/usr/bin/env python3

def main():
    
    with open("input.txt") as f:
        data = [int(i) for i in f.read().split(",")]

    max_pos = max(data)
    least_fuel = -1

    for a in range(max_pos):

        fuel_count = 0

        for b in data:
            n = abs(a - b) # steps walked 
            fuel_count += (n * (n + 1)) // 2 # fuel consumption for n steps = Triangular number at n

        if fuel_count < least_fuel or least_fuel == -1:
            least_fuel = fuel_count

    print(least_fuel)


if __name__ == "__main__":
    main()
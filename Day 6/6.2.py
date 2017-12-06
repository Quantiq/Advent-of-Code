#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        memory_banks = [int(i) for i in f.read().split()]
        
    cycles, seen = 0, {}

    while True:
        cycles += 1
        n, index = max(memory_banks), memory_banks.index(max(memory_banks))
        memory_banks[index] = 0

        for i in range(n):
            index += 1
            if index > len(memory_banks) - 1:
                index = 0
            memory_banks[index] += 1
        current_state = tuple(memory_banks)

        if current_state in seen:
            print(cycles - seen[current_state])
            break
        else:
            seen[current_state] = cycles


if __name__ == '__main__':
    main()
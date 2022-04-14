#!/usr/bin/env python3

def main():

    with open("input.txt") as f:
        data = [i for i in f.read().splitlines()]
        
    gamma, epsilon = [], []
    one_bits, zero_bits = 0, 0

    for bitposition in range(len(data[0])):

        # counter
        for i in data:
            if i[bitposition] == '0':
                zero_bits += 1
            if i[bitposition] == '1':
                one_bits += 1

        if zero_bits > one_bits:
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')

        one_bits, zero_bits = 0, 0

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    power_consumption = gamma * epsilon

    print(power_consumption)

if __name__ == '__main__':
    main()
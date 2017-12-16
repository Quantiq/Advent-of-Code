#!/usr/bin/env python3

import operator

def main():
    with open("input.txt") as f:
        content = [i.split() for i in f.read().splitlines()]

    registers = {lines[0]: 0 for lines in content}
    l_max = 0

    for lines in content:
        key_a = lines[0]
        op_a = lines[1]
        num_a = int(lines[2])
        
        key_b = lines[4]
        op_b = lines[5]
        num_b = int(lines[6])

        if evaluate_condition(registers, key_b, op_b, num_b):
            l_max = update_registers(l_max, registers, key_a, op_a, num_a)

    print(l_max)


def evaluate_condition(registers, key, condition, num):
    condition_table = {
        '==': operator.eq,
        '!=': operator.ne,
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge,
    }
    
    return condition_table[condition](registers[key], num)


def update_registers(l_max, registers, key, condition, num):
    if condition == 'inc':
        registers[key] += num
    elif condition == 'dec':
        registers[key] -= num

    if registers[key] > l_max:
        l_max = registers[key]
    return l_max


if __name__ == '__main__':
    main()
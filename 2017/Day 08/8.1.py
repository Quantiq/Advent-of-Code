#!/usr/bin/env python3

import operator

def main():
    with open("input.txt") as f:
        content = [i.split() for i in f.read().splitlines()]
    
    registers = {lines[0]: 0 for lines in content}

    for lines in content:
        key_a = lines[0]
        op_a = lines[1]
        num_a = int(lines[2])
        
        key_b = lines[4]
        op_b = lines[5]
        num_b = int(lines[6])

        if evaluate_condition(registers, key_b, op_b, num_b):
            registers = update_registers(registers, key_a, op_a, num_a)

    print(max(registers.values()))


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


def update_registers(registers, key, condition, num):
    if condition == 'inc':
        registers[key] += num
    elif condition == 'dec':
        registers[key] -= num
    return registers


if __name__ == '__main__':
    main()
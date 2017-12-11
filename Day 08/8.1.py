#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = [i.split() for i in f.read().splitlines()]

    for lines in content:
        registers[lines[0]] = 0

    for lines in content:
        key_to_change = lines[0]
        add_sub = lines[1]
        num_to_change_by = int(lines[2])
        
        condition_key = lines[4]
        condition = lines[5]
        condition_num = int(lines[6])

        if evaluate_condition(registers, condition_key, condition, condition_num):
            registers = update_registers(registers, key_to_change, add_sub, num_to_change_by)

    print(max(registers.values()))


def evaluate_condition(registers, key, condition, num):
    if condition == '==':
        return registers[key] == num
    elif condition == '!=':
        return registers[key] != num
    elif condition == '<':
        return registers[key] < num
    elif condition == '<=':
        return registers[key] <= num
    elif condition == '>':
        return registers[key] > num
    elif condition == '>=':
        return registers[key] >= num


def update_registers(registers, key, add_sub, num):
    if add_sub == 'inc':
        registers[key] += num
    elif add_sub == 'dec':
        registers[key] -= num
    return registers


if __name__ == '__main__':
    main()
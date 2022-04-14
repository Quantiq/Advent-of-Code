#!/usr/bin/env python3

def main():

    decoded_output_values = []

    with open("input.txt") as f:
        data = [[i.split() for i in j.split(" | ")] for j in f.read().splitlines()]

    for line in data:
        decoded_output_values.append(decode(line[0], line[1]))
              
    print(sum(decoded_output_values))


def decode(signal_patterns_line, output_line):
    # decode output line

    decoded_numbers = []
    one, four, seven = get_known(signal_patterns_line)


    for string in output_line:

        if len(string) == 2:
            decoded_numbers.append(1)

        if len(string) == 3:
            decoded_numbers.append(7)
        
        if len(string) == 4:
            decoded_numbers.append(4)
        
        if len(string) == 7:
            decoded_numbers.append(8)

        if len(string) == 5:

            if all(i in string for i in one):           # if all segments from 1 in string, then it is 3.
                decoded_numbers.append(3)

            else:
                count = 0
                for letter in string:                   # if 3 segments from 4 in string, then string is 5, else it is 2.
                    if letter in four:
                        count += 1
                if count == 3:
                    decoded_numbers.append(5)
                else:
                    decoded_numbers.append(2)

        if len(string) == 6:

            if not all(i in string for i in seven):     # if all segments from 7 in string, then it is 6.
                decoded_numbers.append(6)

            elif all(i in string for i in four):        # if all segments from 4 in string, then it is 9, else it is 0.
                decoded_numbers.append(9)

            else:
                decoded_numbers.append(0)

    return int("".join(map(str, decoded_numbers)))


def get_known(line):
    # get known numbers from unique string lengths

    for string in line:

        if len(string) == 2:
            one = string
            
        if len(string) == 4:
            four = string

        if len(string) == 3:
            seven = string

    return one, four, seven


if __name__ == "__main__":
    main()
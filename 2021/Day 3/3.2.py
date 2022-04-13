#!/usr/bin/env python3

def main():
    
    with open("input.txt") as f:
        data = [i for i in f.read().splitlines()]
    
    oxygen_generator_rating = data.copy()
    co2_scrubber_rating = data.copy()

    # find oxygen generator rating    
    for bitposition in range(len(data[0])):

        if len(oxygen_generator_rating) == 1:
            break

        one_bits, zero_bits = 0, 0

        # counter
        for i in oxygen_generator_rating:
            if i[bitposition] == '1':
                one_bits += 1
            else:
                zero_bits += 1
        
        # let greater values at bitposition = oxygen generator rating, unless 1s and 0s are equal in which case add 1s
        if one_bits >= zero_bits:
            oxygen_generator_rating = [i for i in oxygen_generator_rating if i[bitposition] == '1']
        else:
            oxygen_generator_rating = [i for i in oxygen_generator_rating if i[bitposition] == '0']

    # find co2 scrubber rating
    for bitposition in range(len(data[0])):

        if len(co2_scrubber_rating) == 1:
            break

        one_bits, zero_bits = 0, 0

        # counter
        for i in co2_scrubber_rating:
            if i[bitposition] == '1':
                one_bits += 1
            else:
                zero_bits += 1
        
        # let lesser values at bitposition = co2 scrubber rating, unless 1s and 0s are equal in which case add 0s
        if one_bits < zero_bits:
            co2_scrubber_rating = [i for i in co2_scrubber_rating if i[bitposition] == '1']
        else:
            co2_scrubber_rating = [i for i in co2_scrubber_rating if i[bitposition] == '0']

    product = bin_to_int(oxygen_generator_rating[0]) * bin_to_int(co2_scrubber_rating[0])
    print(product)

def bin_to_int(input):
    # convert binary string to decimal integer
    return int(input, 2)

if __name__ == "__main__":
    main()
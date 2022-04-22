#!/usr/bin/env python3

from collections import Counter

def main():
    
    with open('input.txt') as f:
        data = f.read().splitlines()
    
    pairs = [i for i in data[0]]                           # get intial list of letters from polymer string
    pair_rules = [([i[0], i[1], i[6]]) for i in data[2:]]  # create list of pair insertion rules from data
    steps = 10                                             # set number of steps to iterate

    for step in range(steps):

        new_pairs = pairs.copy()
        offset = 0       # offset

        for i in range(len(pairs) - 1):
            for rule in pair_rules:

                left_side = rule[0]
                right_side = rule[1]
                letter_to_insert = rule[2]

                if left_side == pairs[i] and right_side == pairs[i + 1]:   # if LS and RS are a match:
                    new_pairs.insert(i + 1 + offset, letter_to_insert)     # insert letter
                    offset += 1                                            # add 1 to offset
        pairs = new_pairs

    m_common = Counter(pairs).most_common()[0]     # count most common letter
    l_common = Counter(pairs).most_common()[-1]    # count least common letter

    print(m_common[1] - l_common[1])


if __name__ == '__main__':
    main()
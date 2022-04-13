#!/usr/bin/env python3

from functools import reduce

def main():
    string_input = "stpzcrnm"
    key_strings = [string_input + "-" + str(i) for i in range(128)]
    hashes = list(map(lambda x: binary_knot_hasher(x), key_strings))

    hash_coords = []

    for x, row in enumerate(hashes):
        for y, col in enumerate(row):
            if int(col):
                hash_coords.append((x, y))

    count = 0

    while hash_coords:
        for x, y in hash_coords:
            count += 1
            recursive_find(hash_coords, x, y)
            break

    print(count)


def recursive_find(hash_coords, x, y):
    if (x, y) not in hash_coords:
        return
    else:
        hash_coords.remove((x, y))
        recursive_find(hash_coords, x - 1, y)    # left
        recursive_find(hash_coords, x + 1, y)    # right
        recursive_find(hash_coords, x, y + 1)    # up
        recursive_find(hash_coords, x, y - 1)    # down


def binary_knot_hasher(str_input):
    sparse_hash = sparse_hasher([ord(i) for i in str_input])
    knot_hash = ""

    for i in range(0, 256, 16):
        dense_hash = reduce(lambda x, y: x^y, sparse_hash[i:i+16])
        knot_hash += "{:08b}".format(dense_hash)

    return knot_hash


def sparse_hasher(lengths):
    lengths += [17, 31, 73, 47, 23]
    sparse_hash = list(range(0, 256))
    start_index, skip_size, hash_len = 0, 0, len(sparse_hash)

    for i in range(64):
        for length in lengths:
            end_index = (start_index + length) % hash_len

            if length == 0:
                start_index = (start_index + skip_size) % hash_len
                skip_size += 1
                continue
            elif end_index <= start_index:
                reversed_list = sparse_hash[:end_index][::-1] + sparse_hash[start_index:][::-1]
                index_to_change = start_index
                for i in reversed_list:
                    index_to_change %= hash_len
                    sparse_hash[index_to_change] = i
                    index_to_change += 1
            else:
                sparse_hash[start_index:end_index] = sparse_hash[start_index:end_index][::-1]

            start_index = (start_index + length + skip_size) % hash_len
            skip_size += 1
    return sparse_hash


if __name__ == '__main__':
    main()
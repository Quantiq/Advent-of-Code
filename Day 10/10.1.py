#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        lengths = [int(i) for i in f.read().split(',')]

    sparse_hash = sparse_hasher(lengths)
    print(sparse_hash[0] * sparse_hash[1])


def sparse_hasher(lengths):
    sparse_hash = list(range(0, 256))
    start_index, skip_size, hash_len = 0, 0, len(sparse_hash)

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
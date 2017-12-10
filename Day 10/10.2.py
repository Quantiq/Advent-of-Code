def main():
    with open("testinput.txt") as f:
        lengths = [ord(i) for i in f.read()]

    sparse_hash = sparse_hasher(lengths)
    knot_hash = ""

    for i in range(0,256,16):
        n = dense_hasher(sparse_hash[i:i+16])
        knot_hash += "{:02x}".format(n)
    
    print(knot_hash)

    # test = "7f94112db4e32e19cf6502073c66f9bb"
    # if knot_hash == test:
    #     print("Yes")

def dense_hasher(hash_block):
    n = hash_block[0] ^ hash_block[1]
    for i in range(2, len(hash_block)):
        n ^= hash_block[i]
    return n


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
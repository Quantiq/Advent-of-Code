

def main():
    # with open("testinput.txt") as f:
    #     lengths = [int(i) for i in f.read().split(',')]
    # hash_list = list(range(0,5))

    with open("input.txt") as f:
        lengths = [int(i) for i in f.read().split(',')]
    hash_list = list(range(0,256))

    print(hash_list)
    print(lengths)
    print(len(hash_list))

    # n % len() = wrap
    start_index, skip_size = 0, 0

    for length in lengths:
        print(length)
        end_index = ((start_index + length) % len(hash_list))
        # print(hash_list)
        print(f"start: {start_index}")
        print(f"end: {end_index}")

        if length == 0:
            start_index = (start_index + length + skip_size) % len(hash_list)
            skip_size += 1
            continue

        if end_index <= start_index:
            reversed_list = hash_list[:end_index][::-1] + hash_list[start_index:][::-1]

            index_to_change = start_index
            for i in reversed_list:
                if index_to_change > len(hash_list) - 1:
                    index_to_change = 0
                hash_list[index_to_change] = i
                index_to_change += 1
        else:
            hash_list[start_index:end_index] = hash_list[start_index:end_index][::-1]
        
        start_index = (start_index + length + skip_size) % len(hash_list)
        skip_size += 1
        print(hash_list)
        print("")

    print("val is: {}".format(hash_list[0] * hash_list[1]))


if __name__ == '__main__':
    main()
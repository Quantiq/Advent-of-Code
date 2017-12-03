#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = list(f.read())

    A = content[len(content)//2:]
    B = content[:len(content)//2]
    total = 0

    for i in range(len(A)):
        if int(A[i]) == int(B[i]):
            total += int(A[i]) + int(B[i])
    print(total)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = [int(i) for i in f.read().strip()]

    A = content[len(content)//2:]
    B = content[:len(content)//2]
    total = 0

    for i in range(len(A)):
        if A[i] == B[i]:
            total += A[i] + B[i]
    print(total)


if __name__ == '__main__':
    main()
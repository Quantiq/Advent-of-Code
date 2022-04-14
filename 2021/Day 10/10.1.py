#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        data = [[str(i) for i in j] for j in f.read().splitlines()]

    score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
    brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
    score = 0

    for line in data:

        stack = []

        for char in line:
            if char in "([{<":
                stack.append(char)
            elif brackets[char] != stack.pop():
                score += score_dict[char]
                break
    
    print(score)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        data = [[str(i) for i in j] for j in f.read().splitlines()]

    score_dict = {"(": 1, "[": 2, "{": 3, "<": 4}
    brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
    scores = []

    for line in data:

        stack = []
        noerror = True

        for char in line:
            if char in "([{<":
                stack.append(char)
            elif brackets[char] != stack.pop():
                noerror = False
                break
        
        if noerror:
            stack.reverse()
            score = 0
            for i in stack:
                score = score * 5 + score_dict[i]
            scores.append(score)

    scores.sort()
    print(scores[len(scores) // 2])


if __name__ == "__main__":
    main()
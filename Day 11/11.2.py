#!/usr/bin/env python3

def main():
    with open("input.txt") as f:
        content = f.read().strip().split(',')

        x, y, z, local_max = 0, 0, 0, 0

        for i in content:
            if i == 'n':
                y += 1
                z -= 1
            elif i == 'ne':
                x += 1
                z -= 1
            elif i == 'nw':
                x -= 1
                y += 1
            elif i == 's':
                y -= 1
                z += 1
            elif i == 'se':
                x += 1
                y -= 1
            elif i == 'sw':
                x -= 1
                z += 1
            
            total = abs(x) + abs(y) + abs(z)

            if total > local_max:
                local_max = total
        
        print(local_max // 2)


if __name__ == '__main__':
    main()
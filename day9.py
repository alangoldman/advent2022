import numpy as np

file = open("day9.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

seen = set()

head = [0, 0]
tail = [0, 0]
for line in lines:
    for i in range(int(line[2:])):
        if line[0] == 'R':
            head[0] += 1
        if line[0] == 'U':
            head[1] += 1
        if line[0] == 'L':
            head[0] -= 1
        if line[0] == 'D':
            head[1] -= 1
            
        dx = abs(head[0] - tail[0])
        dy = abs(head[1] - tail[1])
        far = dx > 1 or dy > 1
        #print('head moves', line, head, tail, far)
        
        if far:
            if dx >= 1 and dy >= 1:
                # diag case
                if dx == 1:
                    tail[0] = head[0]
                if dy == 1:
                    tail[1] = head[1]
            if dx > 1:
                tail[0] = int((head[0] + tail[0])/2)
            if dy > 1:
                tail[1] = int((head[1] + tail[1])/2)

        dx = abs(head[0] - tail[0])
        dy = abs(head[1] - tail[1])
        far = dx > 1 or dy > 1
        print('tail moves', line, head, tail, far, dx, dy)
        seen.add((tail[0], tail[1]))
print(len(seen))
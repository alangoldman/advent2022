import numpy as np

file = open("day9.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

seen = set()

def move_section(head, tail):
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

snake = np.zeros((10, 2))
for line in lines:
    for i in range(int(line[2:])):
        # move head
        if line[0] == 'R':
            snake[0][0] += 1
        if line[0] == 'U':
            snake[0][1] += 1
        if line[0] == 'L':
            snake[0][0] -= 1
        if line[0] == 'D':
            snake[0][1] -= 1   

        # move each tail piece
        for i in range(1, len(snake)):
            move_section(snake[i-1], snake[i])
        seen.add((snake[-1][0], snake[-1][1]))
print(len(seen))
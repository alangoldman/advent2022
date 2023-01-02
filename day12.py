import numpy as np

file = open("day12.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

heightmap = np.zeros(shape=(len(lines), len(lines[0])))
grid = np.zeros(shape=(len(lines), len(lines[0])))
for r in range(len(lines)):
    for c in range(len(lines[0])):
        heightmap[r, c] = ord(lines[r][c])
        if lines[r][c] == 'E':
            start = (r, c)
            heightmap[start] = ord('z')
        if lines[r][c] == 'S':
            heightmap[r, c] = ord('a')

queue = list()
queue.append(start)

while len(queue) > 0:
    cur = queue.pop(0)
    h = heightmap[cur]
    steps = grid[cur]
    for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        r = cur[0] + dy
        c = cur[1] + dx
        if 0 <= r < heightmap.shape[0] and 0 <= c < heightmap.shape[1] and (heightmap[r, c] >= h-1) and grid[r, c] == 0:
            grid[r, c] = steps + 1
            queue.append((r, c))
            if heightmap[r, c] == ord('a'):
                print(steps+1)
                queue = [] # exit
                break
    
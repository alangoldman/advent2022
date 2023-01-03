import numpy as np

file = open("day14.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

grid = np.full((200, 1000), False)
max_depth = 0
for line in lines:
    path = line.split(' -> ')
    print(path)
    prev_point = None
    for point in path:
        x, y = [int(i) for i in point.split(',')]
        max_depth = max(max_depth, y)
        if prev_point is not None:
            if x == prev_point[0]:
                first, second = y, prev_point[1]
                if first > second:
                    first, second = second, first
                grid[first:second+1, x] = True
            elif y == prev_point[1]:
                first, second = x, prev_point[0]
                if first > second:
                    first, second = second, first
                grid[y, first:second+1] = True
            else:
                print("shouldn't be here")
        prev_point = x, y

count = 0
while True:
    cur = 0, 500
    settled = False
    while not settled and cur[0] < grid.shape[0]-1:
        settled = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            next = cur[0]+dy, cur[1]+dx
            if not grid[next]:
                cur = next
                settled = False
                break
    if settled:
        grid[cur] = True
        count += 1
    else:
        break

print(count)
print(grid[0:10, 495:505])
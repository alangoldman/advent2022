import numpy as np

file = open("day8.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

heightmap = np.zeros((len(lines), len(lines[0])), int)
visible = np.ones((len(lines), len(lines[0]), 4), bool)


for j in range(len(lines)):
    for i in range(len(lines[0])):
        heightmap[j][i] = int(lines[j][i])
        

for j in range(1, len(lines)-1):
    west_max = heightmap[j][0]
    for i in range(1, len(lines[0])-1):
        if heightmap[j][i] <= west_max:
            visible[j][i][0] = False
            #print(j, i, False, 'west')
        else:
            west_max = heightmap[j][i]
            
    east_max = heightmap[j][-1]
    for i in range(len(lines[0])-2, 0, -1):
        if heightmap[j][i] <= east_max:
            visible[j][i][1] = False
            #print(j, i, False, 'east')
        else:
            east_max = heightmap[j][i]
            
for i in range(1, len(lines[0])-1):
    north_max = heightmap[0][i]
    for j in range(1, len(lines)-1):
        if heightmap[j][i] <= north_max:
            visible[j][i][2] = False
            #print(j, i, False, 'north')
        else:
            north_max = heightmap[j][i]
            
    south_max = heightmap[-1][i]
    for j in range(len(lines)-2, 0, -1):
        if heightmap[j][i] <= south_max:
            visible[j][i][3] = False
            #print(j, i, False, 'south')
        else:
            south_max = heightmap[j][i]

def tree_score(heightmap, y, x):
    score = 1
    max_view = heightmap[y][x]
    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        j = y + dy
        i = x + dx
        dist = 0
        while j >= 0 and j < len(lines) and i >= 0 and i < len(lines[0]):
            dist += 1
            if heightmap[j][i] >= max_view:
                break
            j += dy
            i += dx
        
        score *= dist
    return score
            
count = 0
best = None
for j in range(1, len(lines)-1):
    for i in range(1, len(lines[0])-1):
        if (any(visible[j][i])):
            count += 1
            score = tree_score(heightmap, j, i)
            if best is None or score > best[0]:
                best = (score, j, i)
                
print(count)
print(best)
#print(visible)
#print(heightmap)

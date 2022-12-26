import numpy as np

file = open("day10.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

queue = list()
cycle = 1
x = 1
isp = 0
count = 0
while isp < len(lines) or len(queue) > 0:
    if len(queue) == 0 and isp <= len(lines):
        line = lines[isp-1]
        isp += 1
        if line == 'noop':
            pass
        else:
            op, value = line.split(' ')
            clock_cycles = 2  # only addx for now
            queue.append([(op, int(value)), clock_cycles])

    for i in range(0, len(queue)):
        queue[i][1] -= 1
        if queue[i][1] == 0:
            x += queue[i][0][1]
    queue = [q for q in queue if q[1] > 0]
    #print(cycle, x, len(queue))
    if cycle == 20 or (cycle-20)%40 == 0:
        print(cycle, x)
        count += cycle*x
    cycle += 1

print(count)
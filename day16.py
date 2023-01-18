import numpy as np
import re

file = open("day16.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

graph = {}
for line in lines:
    first, second = line.split(';')
    valve = first[6:8]
    rate = int(first.split('=')[1])
    
    adj = [a.strip() for a in second.replace('valve', 'valves')[24:].split(', ')]
    
    graph[valve] = (rate, adj, -1)
    
queue = list()
seen = set()
# steps, score, position, opened valves
queue.append((30, 0, 'AA', set()))
seen.add((0, 'AA', ''))
best = None
print(graph)

def set_to_string(s):
    return ''.join([c for c in s])

while len(queue)>0:
    steps, score, cur, valves = queue.pop(0)
    steps -= 1

    flow, adj, _ = graph[cur]
    #print(steps, score, cur, valves)
    if steps == 0 or len(valves) == len(graph.keys()):
        if  len(valves) == len(graph.keys()):
            print('early!')
        if best is None or score > best:
            best = score
        continue
    
    if cur not in valves:
        # try opening the valve
        new_score = score+flow*steps
        valves2 = valves.union(set([cur]))
        if (new_score, cur, set_to_string(valves)) not in seen:
            seen.add((new_score, cur, set_to_string(valves2)))
            queue.append((steps, new_score, cur, valves2))

    for edge in adj:
        if (score, edge, set_to_string(valves)) not in seen:
            seen.add((score, edge, set_to_string(valves)))
            queue.append((steps, score, edge, valves))

print(best)
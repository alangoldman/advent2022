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

def best_score(steps, score, valves):
    for valve in set(graph.keys()).difference(valves):
        score += steps*graph[valve][0]
    return score

def test_deadend(steps, score, valves, best):
    if best is None:
        return False
    return best_score(steps, score, valves) > best

while len(queue)>0:
    steps, score, cur, valves = queue.pop(0)
    cur_best_score = best_score(steps, score, valves)
    if graph[cur][2] != -1 and cur_best_score < graph[cur][2]:
        print('skip')
        continue
    steps -= 1

    flow, adj, _ = graph[cur]
    #print(steps, score, cur, valves)
    if steps == 0 or len(valves) == len(graph.keys()) or test_deadend(steps, score, valves, best):
        if  len(valves) == len(graph.keys()) or test_deadend(steps, score, valves, best):
            print('early!')
        if best is None or score > best:
            best = score
        continue
    
    if cur not in valves:
        # try opening the valve
        new_score = score+flow*steps
        valves2 = valves.union(set([cur]))
        new_best_score = best_score(steps, new_score, valves2)
        if (new_score, cur, set_to_string(valves)) not in seen or new_best_score > graph[cur][2]:
            seen.add((new_score, cur, set_to_string(valves2)))
            graph[cur] = (graph[cur][0], graph[cur][1], new_best_score)
            queue.append((steps, new_score, cur, valves2))

    for edge in adj:
        if (score, edge, set_to_string(valves)) not in seen or cur_best_score > graph[edge][2]:
            seen.add((score, edge, set_to_string(valves)))
            graph[edge] = (graph[edge][0], graph[edge][1], cur_best_score)
            queue.append((steps, score, edge, valves))

print(best)
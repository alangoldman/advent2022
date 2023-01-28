import numpy as np
import re

file = open("day16.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

valve_index = 0
valve_list = []
graph = {}
for line in lines:
    first, second = line.split(';')
    valve = first[6:8]
    rate = int(first.split('=')[1])
    
    adj = [a.strip() for a in second.replace('valve', 'valves')[24:].split(', ')]
    
    graph[valve] = (rate, adj, valve_index)
    valve_list.append(valve)
    valve_index += 1
    
dist = np.full((len(graph.keys()), len(graph.keys())), 1000000)

# floyd-warshall
for valve in graph.keys():
    flow, adj, index = graph[valve]
    dist[index][index] = 0
    for edge in adj:
        dist[index][graph[edge][2]] = 1
for k in range(0, len(valve_list)):
    for i in range(0, len(valve_list)):
        for j in range(0, len(valve_list)):
            composite_dist = dist[i, k] + dist[k, j]
            dist[i, j] = min(dist[i, j], composite_dist)


queue = list()
seen = set()
# steps, score, position, opened valves
queue.append((30, 0, 'AA', set()))
seen.add((30, 'AA', ''))
best = None
print(graph)

def set_to_string(s):
    return ''.join([c for c in s])

while len(queue)>0:
    steps, score, cur, valves = queue.pop(0)

    flow, adj, index = graph[cur]
    #print(steps, score, cur, valves)
    if best is None or score > best:
        best = score

    for valve in graph.keys():
        if graph[valve][0] > 0 and valve not in valves:
            steps2 = steps - dist[graph[cur][2], graph[valve][2]] - 1
            if steps2 < 0:
                continue
            score2 = score + steps2 * graph[valve][0]
            valves2 = valves.union(set([valve]))
            if (steps2, valve, set_to_string(valves2)) not in seen:
                seen.add((score2, steps2, set_to_string(valves2)))
                queue.append((steps2, score2, valve, valves2))

print(best)
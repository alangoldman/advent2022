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
seen = {}
# steps, score, position, opened valves
queue.append((26, 26, 0, 'AA', 'AA', set()))
# max_steps, pos, pos, opened valves (string): score
seen[((26, 'AA', 'AA', ''))] = 0
best = 0
print(graph)

def set_to_string(s):
    return ''.join([c for c in s])
    
def best_possible_remaining_score(steps, valves):
    score = 0
    for valve in graph.keys():
        if valve not in valves:
            score += (steps-1) * graph[valve][0]
    return score

while len(queue)>0:
    steps, steps_e, score, cur, cur_e, valves = queue.pop()

    #print(steps, steps_e, score, cur, cur_e, valves)
        
    if score + best_possible_remaining_score(max(steps, steps_e), valves) < best:
        continue

    next_moves = []
    # my turn
    flow, adj, index = graph[cur]
    for valve in graph.keys():
        if graph[valve][0] > 0 and valve not in valves:
            steps2 = steps - dist[graph[cur][2], graph[valve][2]] - 1
            if steps2 < 0:
                continue
            score2 = score + steps2 * graph[valve][0]
            valves2 = valves.union(set([valve]))
            pos = sorted([valve, cur_e])
            key = (max(steps, steps_e), pos[0], pos[1], set_to_string(valves2))
            if key not in seen or seen[key] < score2:
                seen[key] = score2
                next_moves.append((steps2, steps_e, score2, valve, cur_e, valves2))
                
    flow, adj, index = graph[cur_e]
    for valve in graph.keys():
        if graph[valve][0] > 0 and valve not in valves:
            steps2 = steps_e - dist[graph[cur_e][2], graph[valve][2]] - 1
            if steps2 < 0:
                continue
            score2 = score + steps2 * graph[valve][0]
            valves2 = valves.union(set([valve]))
            pos = sorted([cur, valve])
            key = (max(steps, steps_e), pos[0], pos[1], set_to_string(valves2))
            if key not in seen or seen[key] < score2:
                seen[key] = score2
                next_moves.append((steps, steps2, score2, cur, valve, valves2))
               
    if len(next_moves) == 0 and score > best:
        best = score
        print('New best!', best, ',memo size:', len(seen.keys()))
    #next_moves = sorted(next_moves, key=lambda x: x[2]+best_possible_remaining_score(max(x[0], x[1]), x[3]), reverse=True)
    next_moves = sorted(next_moves, key=lambda x: x[2], reverse=True)
    queue += next_moves

print(best)
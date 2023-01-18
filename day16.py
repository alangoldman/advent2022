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
    
    graph[valve] = (rate, adj)
    
queue = list()
seen = set()
# steps, score, position, opened valves
queue.append((26, 0, 'AA', 'AA', True, set()))
seen.add((0, 'AA', 'AA', True, ''))
best = None
print(graph)

def set_to_string(s):
    return ''.join([c for c in s])

while len(queue)>0:
    steps, score, cur, ele, my_turn, valves = queue.pop(0)
    if my_turn:
        steps -= 1

    #print(steps, score, cur, ele, my_turn, valves)
    if steps == 0 or len(valves) == len(graph.keys()):
        if  len(valves) == len(graph.keys()):
            print('early!')
        if best is None or score > best:
            best = score
        continue
    
    if my_turn:
        flow, adj = graph[cur]
        next_states = adj if cur in valves else adj + ['open']
        
        for edge in next_states:
            if edge == 'open':
                # try opening the valve
                new_score = score+flow*steps
                valves2 = valves.union(set([cur]))
                if (new_score, cur, ele, my_turn, set_to_string(valves2)) not in seen:
                    seen.add((new_score, cur, ele, my_turn, set_to_string(valves2)))
                    queue.append((steps, new_score, cur, ele, False, valves2))
            elif (score, edge, ele, my_turn, set_to_string(valves)) not in seen:
                seen.add((score, edge, ele, my_turn, set_to_string(valves)))
                queue.append((steps, score, edge, ele, False, valves))
    else:
        flow, adj = graph[ele]
        next_states = adj if ele in valves else adj + ['open']
        
        for edge in next_states:
            if edge == 'open':
                # try opening the valve
                new_score = score+flow*steps
                valves2 = valves.union(set([ele]))
                if (new_score, cur, ele, my_turn, set_to_string(valves2)) not in seen:
                    seen.add((new_score, cur, ele, my_turn, set_to_string(valves2)))
                    queue.append((steps, new_score, cur, ele, True, valves2))
            elif (score, cur, edge, my_turn, set_to_string(valves)) not in seen:
                seen.add((score, cur, edge, my_turn, set_to_string(valves)))
                queue.append((steps, score, cur, edge, True, valves))


print(best)
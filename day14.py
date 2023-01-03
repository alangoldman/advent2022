import numpy as np

file = open("day14.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

for line in lines:
    path = line.split(' -> ')
    for x, y in path:
        print(x, y)
import numpy as np
import re

file = open("day15.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

y_final = 2000000
ranges = list()

def dist(sensor, beacon):
    return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

beacons = set()
for line in lines:
    pattern = re.compile(r"Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)", re.IGNORECASE)
    m = pattern.match(line)
    sensor, beacon = (int(m[1]), int(m[2])), (int(m[3]), int(m[4]))

    r = dist(sensor, beacon)
    tangent_y = dist(sensor, (sensor[0], y_final))
    if tangent_y <= r:
        tangent_x = r - tangent_y
        if tangent_x == 1:
            ranges.append((sensor[0], sensor[0]))
        else:
            ranges.append((sensor[0]-tangent_x, sensor[0]+tangent_x))
            
    if beacon[1] == y_final:
        beacons.add(beacon[0])

def remove_beacons(range):
    count = 0
    for beacon in beacons:
        if range[0] <= beacon <= range[1]:
            count += 1
    if count > 0:
        print("remove_beacons", range, count)
    return count

ranges.sort()
print(ranges, beacons)
last_range = None
count = 0
for range in ranges:
    if last_range is None:
        count += range[1] - range[0] + 1
        count -= remove_beacons(range)
    elif range[0] <= last_range[1]:
        if range[1] <= last_range[1]:
            pass
        else:
            count += range[1] - last_range[1]
            count -= remove_beacons((last_range[1]+1, range[1]))
    else:
        count += range[1] - range[0] + 1
        count -= remove_beacons(range)
    print(range, count)
    if last_range is None:
        last_range = range
    else:
        last_range = (min(range[0], last_range[0]), max(range[1], last_range[1]))
        
    
print(count)
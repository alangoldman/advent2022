import numpy as np
from functools import cmp_to_key

file = open("day13.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

def compare(left, right):
    #print('comparing', left, right)
    if type(left) is int and type(right) is int:
        if left == right:
            return None
        return left <= right
    elif type(left) is list and type(right) is list:
        for i in range(min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result == None:
                continue
            else:
                return result
        if len(left) == len(right):
            return None
        return len(left) < len(right)
    elif type(left) is not list:
        return compare([left], right)
    elif type(right) is not list:
        return compare(left, [right])

    return False  # shouldn't be hit

def _compare(left, right):
    result = compare(left, right)
    if result == None:
        return 0
    return -1 if result else 1

count = 0
l = None
r = None
pair = 0
packets = []
for i in range(len(lines)):
    if lines[i].strip() == '':
        continue
    if l is None:
        l = eval(lines[i])
    elif r is None:
        r = eval(lines[i])
        packets.append(l)
        packets.append(r)
        pair += 1

        in_order = compare(l, r)
        print(l, r, in_order)
        if in_order or in_order is None:
            count += pair
            
        l = None
        r = None

d1 = [[2]]
d2 = [[6]]
packets.append(d1)
packets.append(d2)
packets.sort(key=cmp_to_key(_compare))

print((packets.index(d1)+1)*(packets.index(d2)+1))
print(count)
import numpy as np

file = open("day11.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

monkeys = []
monkey = None
for i in range(0, len(lines)):
    if lines[i].startswith('Monkey'):
        held = [int(item) for item in lines[i+1][16:].split(', ')]
        op = lines[i+2][21]
        operand = lines[i+2][23:]
        test = int(lines[i+3][19:])
        true_monkey = int(lines[i+4][25:])
        false_monkey = int(lines[i+5][26:])
        monkeys.append([held, op, operand, test, true_monkey, false_monkey, 0])
        i += 5
        
for r in range(1, 21):
    for i in range(len(monkeys)):
        held, op, operand, test, true_monkey, false_monkey, inspections = monkeys[i]
        for item in held:
            if operand == 'old':
                op2 = item
            else:
                op2 = int(operand)
            if op == '*':
                item *= op2
            elif op == '+':
                item += op2
            item = int(item / 3)
            
            if item % test == 0:
                monkeys[true_monkey][0].append(item)
            else:
                monkeys[false_monkey][0].append(item)
                
        monkeys[i][-1] += len(held)
        monkeys[i][0] = []  # nothing held anymore
        
l = sorted([m[-1] for m in monkeys], reverse=True)[0:2]
print(l[0] * l[1])
file = open("day2.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

outcomes = {
    ('A', 'X'): 3+0,
    ('A', 'Y'): 1+3,
    ('A', 'Z'): 2+6,
    ('B', 'X'): 1+0,
    ('B', 'Y'): 2+3,
    ('B', 'Z'): 3+6,
    ('C', 'X'): 2+0,
    ('C', 'Y'): 3+3,
    ('C', 'Z'): 1+6,
}

score = 0
for l in lines:
    p1, p2 = l.split(' ')
    score += outcomes[(p1, p2)]
    
print(score)
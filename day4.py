file = open("day4.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

score = 0
for l in lines:
    a, b = l.split(',')
    s1, e1 = a.split('-')
    s2, e2 = b.split('-')
    s1 = int(s1)
    e1 = int(e1)
    s2 = int(s2)
    e2 = int(e2)
    
    if (not (e1 < s2 or e2 < s1)):
        score += 1
    
print(score)
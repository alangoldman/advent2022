file = open("day3.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

score = 0
for i in range(0, len(lines), 3):
    c = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))
    c = ord(list(c)[0])
    if c <= ord('Z'):
        score += c-ord('A')+27
    else:
        score += c-ord('a')+1
    
print(score)
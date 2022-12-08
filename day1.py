file = open("day1.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

elves = [0]
for l in lines:
    if l == '':
        elves.append(0)
    else:
        elves[-1] += int(l)
print(sum(sorted(elves, reverse=True)[0:3]))
file = open("day6.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

#n=4
n=14
line = lines[0]
for i in range(0, len(line)-n):
    if len(set(line[i:i+n])) == n:
        print(i+n)
        break

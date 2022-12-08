file = open("day5.input.txt", "r")
lines = file.readlines()
file.close()

count = int((len(lines[0])+1)/4)
stacks = list()
for i in range(count):
    stacks.append(list())
build = True
run = False

for l in lines:
    if len(l) > 1 and l[1] == '1':
        build = False
        print('Build done')
        stacks = [[]] + stacks
        for s in stacks:
            print(s)
    elif not build and not run:
        print('Running simulation')
        run = True
    elif build:
        for i in range(count):
            print(i, l, len(l))
            c = l[(i*4)+1]
            if c != ' ':
                stacks[i].append(c)
    elif run:
        _, n, _, start, _, end = l.split(' ')
        t = []
        for i in range(int(n)):
            t.append(stacks[int(start)].pop(0))
        t.reverse()
        for i in range(int(n)):
            stacks[int(end)].insert(0, t[i])

for s in stacks[1:]:
    print(s[0], end='')


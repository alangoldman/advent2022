file = open("day7.input.txt", "r")
lines = file.readlines()
file.close()

lines = [l.strip() for l in lines]

dirs = ['/']
files = {}
cwd = '/'
for i in range(0, len(lines)):
    line = lines[i]
    if line.startswith('$ cd'):
        if line[5]=='/':
            cwd = '/'
        elif line[5:7]=='..':
            cwd = '/'.join(cwd.split('/')[0:-2])+'/'
        else:
            cwd += line[5:]+'/'
            dirs.append(cwd)
    elif line.startswith('$ ls'):
        i += 1
        line = lines[i]
        while i < len(lines) and lines[i][0] != '$':
            line = lines[i]
            if line.startswith('dir'):
                pass
            else:
                size, name = line.split(' ')
                files[cwd+name] = int(size)
            i += 1
        i -= 1
        
#print(files)
#print(dirs)

total = 0
dir_sizes = []
space_left = 70000000
for d in dirs:
    fs = [k for k in files.keys() if k.startswith(d)]
    s = sum([files[f] for f in fs])
    #print(d, s)
    dir_sizes.append((s, d))
    if s <= 100000:
        total += s
    if d == '/':
        space_left -= s
        
#print(total)
print(space_left)
print(sorted(dir_sizes))
for ds in sorted(dir_sizes):
    if space_left + ds[0] > 30000000:
        print(ds)
        break

    

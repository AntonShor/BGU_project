try:
    with open('input.txt', 'r') as text_file:
        ls = text_file.readlines()
except FileNotFoundError:
    print('This file does not exist. Please come back later')

#with open('input.txt', 'r') as text_file:
#    ls = text_file.readlines()

g = []
names = []
for l in ls:
    l= l.strip()
    coma = l.index(',')
    l = l[coma+1::].strip()
    g.append(int(l))
for l in ls:
    l= l.strip()
    coma = l.index(',')
    l = l[:coma].strip()
    names.append(l)

average = sum(g)/len(g)

with open('output.txt', 'w') as text_file:
    for i in range(len(g)):
        if g[i] > average:
            print(names[i], file = text_file)
        

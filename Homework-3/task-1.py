try:
    with open('city.txt', 'r') as text_file:
        lines = text_file.readlines()
        lines.sort()
        ct = []
        pop = []
        a = []
        question = int(input('Enter the number:\n'))
        for i in range(len(lines)):
            line = lines[i].strip()
            colon = line.index(':')
            city = line[:colon]
            ct.append(city)
            population = line[colon+1:]
            pop.append(population)
        for j in range(len(pop)):
            if int(pop[j])>question:
                a.append(ct[j])
                a.append(':')
                a.append(pop[j])
        
        
except FileNotFoundError:
    print('This file does not exist. Please come back later')
    


with open('filtered_ct.txt', 'w') as text_file:
    for k in range(len(a)//3):
        print(*a[3*k:3*(k+1)], sep ='', file = text_file)
       


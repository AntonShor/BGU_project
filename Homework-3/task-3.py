try:
    with open('input.txt', 'r') as text_file:
        ls = text_file.readlines()
        word = input('Write course what you need:\n')
        l = []
        answer=[]
        for i in range(len(ls)):
            l = ls[i]
            l = l.replace(':', ',')
            l = l.split(',')
            for j in range(len(l)):
                x = l[j].strip()    
                if x== word:
                    answer.append(l[0])
    print(*answer, sep ='\n')
        
except FileNotFoundError:
    print('This file does not exist. Please come back later')
    
    
    
    

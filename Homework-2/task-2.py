try:
    with open('input.txt', 'r') as text_file:
        ls = text_file.readlines()
except FileNotFoundError:
    print('This file does not exist. Please come back later')

symbols = input('Enter the symbols to delete:')


    
with open('output.txt', 'w') as text_file:
    for l in ls:
        l = l.rstrip()
        l = l.rstrip(str(symbols))
        l += ';'
        l = l[::-1]
        print(l, file = text_file)
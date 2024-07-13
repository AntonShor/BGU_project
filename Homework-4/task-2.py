def alg_ev(first, second):
    if first == 0 or second == 0:
       return max(first, second)
    else:
        if first > second:
            return alg_ev(first%second, second)
        else:
            return alg_ev(first, second%first)
    
x = int(input('Enter first number'))
y = int(input('Enter second number'))

print('Answer:', alg_ev(x, y))
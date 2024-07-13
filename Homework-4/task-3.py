def steps(a):
    if a < 3:
        return a
    return steps(a - 1) + steps(a - 2)

step = int(input('Enter the amount of steps:'))
print(steps(step))
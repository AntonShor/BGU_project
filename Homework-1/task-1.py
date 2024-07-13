while True:
    number = input("Write a number: ")
    if number.isdigit():
        number = int(number)
        break
    else:
        print("It is not correct. Please enter a valid number.")

for i in range(1, number + 1):
    print((number - i) * ' ' + (2 * i - 1) * '*' + (number - i) * ' ')
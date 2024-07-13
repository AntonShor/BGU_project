
while True:
    a = input("Write a number: ")
    if a.isdigit():
        break
    else:
        print("It is not correct. Please enter a valid number.")

while int(a) > 9:
    k = 0
    for i in range(len(a)):
        k += int(a[i])
    a = str(k)

print(a)
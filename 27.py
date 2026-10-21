lower = int(input("Enter a number: "))
upper = int(input("Enter another number: "))

print("The range of the 2 numbers is" , lower, "to", upper)

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
row_size = int(input("Enter the number of rows: "))

if row_size % 2 == 0:
    half_size = int(row_size/2)
elif row_size % 2 != 0:
    half_size = int((row_size + 1)/2)

space = int(half_size - 1)

for i in range(1, half_size):
    for j in range(1, space + 1):
        print(space, end=" ")
        space -= 1
        number = 1
        for k in range(1, i + 1):
            print(2*i - 1, end=" ")
            print(number)
            number += 1
            print()
            for i in range(half_size-1):
                print(space, end=" ")
                space += 1
                number = 1
                print(2*(half_size - i))
                print(number)
                number += 1
                print()

    

    


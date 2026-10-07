print("Select your ride:")
print("1. Bike")
print("2. Car")


choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("What type of bike?")
    print("1. Mountain Bike")
    print("2. Road Bike")

    choice2 = int(input("Enter your second choice (1 or 2): "))
    if choice2 == 1:
        print("You selected Mountain Bike.")
    else:
        print("You selected Road Bike.")

elif choice == 2:
    print("What type of car?")
    print("1. Sedan")
    print("2. SUV")

    choice3 = int(input("Enter your second choice (1 or 2): "))
    if choice3 == 1:
        print("You selected Sedan.")
    else:
        print("You selected SUV.")
        
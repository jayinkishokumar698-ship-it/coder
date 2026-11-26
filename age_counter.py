try:
    age = int(input("Enter your age: "))

    if age <= 0 or age > 120:
        raise ValueError("Age must be between 1 and 120.")

    print("The age entered is valid.")

    if age % 2 == 0:
        print(f"{age} is an even number.")
    else:
        print(f"{age} is an odd number.")

except ValueError as e:
    print(f"Invalid input! Error: {e}")
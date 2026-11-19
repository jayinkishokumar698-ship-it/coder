import random

playing = True

number = str(random.randint(0,9))

print("Welcome to the guessing game!")
print("I have selected a number between 0 and 9. Can you guess it?")

while playing == True:
    guess = input("Enter your guess: ")
    if guess == number:
        print("Congratulations! The number was", number)
        break
    else:
        print("Sorry, that's not the number. Try again.")
        
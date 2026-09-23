amount = int(input("How much money do you have?"))

note_1 = amount//100
note_2 = (amount%100)//50
note_3 = (amount%100%50)//10

print("Number of $100 notes:", note_1)
print("Number of $50 notes:", note_2)
print("Number of $10 notes:", note_3)
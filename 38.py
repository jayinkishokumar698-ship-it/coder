a = input("Enter a word: ")

for i in range(len(a)):
    if a[i] == "a":
        print("Found 'a' at index", i)
        break
    else:
        print("No 'a' found at index", i)
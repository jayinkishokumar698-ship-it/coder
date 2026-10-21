num = int(input("Enter a number: "))

if num == 0:
    count = 1
else:
    count = 0
    
    while num > 0:
        num = num // 10  
        count += 1      

print(f"Total digits: {count}")
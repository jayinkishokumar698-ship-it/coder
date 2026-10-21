num = int(input("Enter a number: "))
t = num

numlen = 0

while t > 0:
    numlen += 1
    t = t // 10
    if numlen >= 4:
        numlen = int(numlen/2)
        chk = 0 
        while num > 0:
            rem = num % 10
            if chk == numlen:
                mid = rem
            elif chk == (numlen - 1):
                mid2 = rem
            num = int(num/10)
            chk += 1
        prod = mid * mid2
        print(f"The product of the middle two digits is: {prod}")        
    else:
        print("The number does not have enough digits to find the middle two digits.")

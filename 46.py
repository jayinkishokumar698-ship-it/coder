import math 

smallint = math.ceil(23.56)
largeint = math.floor(23.56)

print("The smallest integer greater than or equal to 23.56 is:", smallint, "and the largest integer less than or equal to 23.56 is:", largeint)

x= 10 
y= -15

print("The result of copysign is:", math.copysign(x, y))


print("The absolute value of -96 is:", math.fabs(-96), "and the absolute value of 56 is:", math.fabs(56))

gcd = math.gcd(24, 56)
print("The greatest common divisor of 24 and 56 is:", gcd)
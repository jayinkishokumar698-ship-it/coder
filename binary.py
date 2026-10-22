def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_str = ""
    while n > 0:
        remainder = n % 2        
        binary_str = str(remainder) + binary_str 
        n = n // 2              
        
    return binary_str


decimal_number = float(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_number)

print(f"The binary representation of {decimal_number} is: {binary_result}")
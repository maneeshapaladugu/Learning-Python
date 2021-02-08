#Python program to read 2 numbers and print Qiotient and Remainder

num1 = int(input("Enter number 1\n"))
num2 = int(input("Enter number 2\n"))

if num1 > num2:
    quotient = num1 /num2
    remainder = num1 % num2
else:
    quotient = num2 / num1
    remainder = num2 % num1

print("Quotient: %d" %(quotient))
print("Remainder: %d" %(remainder))

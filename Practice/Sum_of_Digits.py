#Python program to find the sum of digits of given number

def sumDigits(num):
    sum = 0
    while num:
        sum += num % 10
        num = num // 10
    return sum

number = int(input("Enter a number:"))
print("Sum of digits of number %d: %d" %(number, sumDigits(number)))

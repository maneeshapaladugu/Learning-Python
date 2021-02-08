#Python program to count the number of digits of a number

def countDigits(num):
    result = 0
    while num:
        result += 1
        num //= 10
    return result

number = int(input("Enter a number:\n"))
count = countDigits(number)
print("Number of digits of %d is %d" %(number, count))

#Python program to check if a number is Armstrong or not
#If the given number is 153, and 1^3 + 5 ^ 3 + 3 ^ 3 == 153, then 153 is an Armstrong number

def countDigits(num):
    result = 0
    
    while num > 0:
        result += 1
        num //= 10
    print(result)
    return result
    
def isArmstrong(num):
    digitCount = countDigits(num)
    temp = num
    result = 0
    
    while temp:
        result += pow(temp%10, digitCount)
        temp //= 10
        
    if result == num:
        return 1
    else:
        return 0

num = int(input("Enter a number:\n")) #Receive the input as an integer
if isArmstrong(num):
    print("%d is an Armstrong Number" %(num))
else:
    print("%d is not an Armstrong number" %(num))

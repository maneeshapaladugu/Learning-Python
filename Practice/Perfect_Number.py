#Python program to find whether the given number is perfect or not
#If the given number is 6, then sum of successful divisors of 6 == 6, i.e., 1+2+3 is 6, then 6 is a perfect number

def isPerfect(num):
    total = 0
    for i in range(1,num):
        if num%i == 0:
            total += i
    if total == num:
        return 1
    else:
        return 0

num = int(input("Enter a number:\n"))
if (isPerfect(num)):
    print(str(num) + " is a perfect number")
else:
    print(str(num) + " is not perfect number")

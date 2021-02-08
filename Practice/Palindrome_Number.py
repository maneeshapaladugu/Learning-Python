#Python program to find whether given number is palindrome or not
#If the given number is 121, and the reverse of 121 == 121, then 121 is a palindrome number

def isPalindrome(num):
    reverse = 0
    temp = num
    
    while temp:
        reverse = (reverse*10) + (temp%10)
        temp //=10

    if reverse == num:
        return 1
    else:
        return 0
   
num = int(input("Enter a number:\n"))
if isPalindrome(num):
    print(str(num)+ " is a palindrome number")
else:
    print(str(num)+ " is not palindrome number")

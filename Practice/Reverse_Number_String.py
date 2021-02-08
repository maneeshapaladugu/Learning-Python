#Python program to reverse a number

#Method 1:
def reverseNum(n):
    reverse = 0
    while n:
        remainder = n%10
        reverse = reverse * 10 + remainder
        n = n//10 #The purpose of double slash is for floor/integer division
    return reverse

number = int(input("Enter a number\n")) 
print("Reverse of %d is %d" %(number,reverseNum(number)))

#########################################################

#Method 2:
def reverseNum(n):
    reverse = "" #Empty string
    for i in range (len(n)-1,-1,-1): #Loop from string end till start. Decrement position each time.
        reverse = reverse + n[i]
    return int(reverse)

number = int(input("Enter a number\n"))
print("Reverse of %d is %d" %(number,reverseNum(str(number))))

#########################################################

#Python program to reverse a number or a string
#Method 3:
def reverseNumOrString(n):
    reverse = "" #Empty string
    for i in range (len(n)-1,-1,-1): #Loop from string end till start. Decrement position each time.
        reverse = reverse + n[i]
    return reverse

number = input("Enter a Number/String\n")
print("Reverse of %s is %s" %(number,reverseNumOrString(number)))

#########################################################
      
#print(10/3) #Classic division
#3.3333333333333335
#print(10//3)#Floor division
#3

#len("123")
#3
#"12"+"3"
#'123'
#"3"+"2"+"1"
#'321'

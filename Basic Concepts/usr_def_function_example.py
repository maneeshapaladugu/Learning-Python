def hello():
    print('Hello !')
    print('Hello !!!')
    print('Hello World !!!!!')


hello()
hello()
hello()
hello()

#******************************************

def hello(name):
    print('Hello ' + name)

hello('Maneesha')
hello('Manoj')

#**********************************************

print('Maneesha has ' + str(len('Maneesha')) + ' letters in it')
print('Manoj has ' + str(len('Manoj')) + ' letters in it')

#*************************************************

def plusone(number):
    return number + 1

newNumber = plusone(5)
print(newNumber)

#*************************************************

#print() return value is None
#spam = print()
#spam -> has nothing
#spam == None  -> displays True

#************************************************
#print() function call automatically adds new line to the passed string

print('Hello')
print('World')
#Output:
#Hello
#World

#**************************************************

#The print function has keyword arguments end and sep
#Keywords arguments to functions are optional

#Keyword arguement end makes below print() function call without new line at the end of string Hello

print('Hello',end='')#empty end keyword argument 
print('World')
#Output:
#HelloWorld

#When we pass multiple values to the print function, it automatically sepeartes them with a space
print('cat', 'dog', 'mouse')
#Output:
#cat dog mouse

#To set seperate char/string, we can pass the sep keyword argument with a value (seperator)
print('cat', 'dog', 'mouse', sep='ABC')
#Output:
#catABCdogABCmouseABC


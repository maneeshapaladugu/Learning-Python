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
#spam -> diaplys nothing
#spam == None  -> displays True

#************************************************
#Below print() function call automatically adds new line to the passed string
#Output:
#Hello
#World
print('Hello')
print('World')

#**************************************************
#Keywords arguments to functions are optional
#The print function has keyword arguments end and sep

#Keyword arguement end makes below print() function call without new line at the end of string Hello
#Output:
#HelloWorld
print('Hello',end='')
print('World')


#When we pass multiple values to the print finction, it automatically sepeartes them with a space
print('cat', 'dog', 'mouse')
#Output:
#cat dog mouse

#To set seperate char/string instead of a space, we can pass the sep keyword argument
print('cat', 'dog', 'mouse', sep='ABC')
#Output:
#catABCdogABCmouseABC


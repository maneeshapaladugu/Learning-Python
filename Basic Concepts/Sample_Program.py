#Sample program - This program says hello and prompts for name and age

#str(int(age)+1)   #age evaluates to '25'
#str(int('25')+1)  #int('25') evaluates to integer 25 
#str(25+1)         
#str(26)           #str(26) evaluates to string '26'
#'26'

print('Hello! This is Robot')
print('What is your name?')
myname = input()
print('Good to meet you ' + myname)
print('Length of your name:')
print(len(myname))
print('What is your age?')
age = input()
print('Your age will be ' + str(int(age)+1) + ' in an year')
print('Glad to meet you')



#**********************************************************

print('1' + '1') #Output: 11
print("'1' + '1' is " + str('1'+'1')) #Output: 11

print(1+1) #Output: 2
print('1 + 1 is ' + str(1+1)) #Output :1 +1 is 2

#***********************************************************

age = 24
print('Your age will be ' + str(age+1) + ' in an year') #No error

age = input()
print('Your age will be ' + str(int(age)+1) + ' in an year')#Solution to below error

age = input()
print('Your age will be ' + str(age+1) + ' in an year')  #Here age is a string and str(age+1) throws TypeError: can only concatenate str (not "int") to str. 






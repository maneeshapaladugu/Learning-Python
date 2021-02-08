#Python program to print even length words of a given string
#String split method returns a list of strings after breaking the given string by the specified separator

str = input("Enter a string:\n")
str = str.split(' ') #If we don't specify the seperator, the default seperator is also a whitespace

for word in str:
    if len(word)%2 == 0:
        print(word)

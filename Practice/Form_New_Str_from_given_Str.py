#Python program to generate new string out of first 4 and last 4 characters of a given string

string = input("Enter a string:\n")
print("Given string: ", string)
print("Length of given string: ", len(string))

newString = string[0:3] + string[len(string)-3: ]
print("\nNew string : " +newString)
print("Length of new string: ", len(newString))

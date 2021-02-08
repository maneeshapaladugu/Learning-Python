#Python program to count the number of digits and number of letters in a string
letters = 0
digits = 0
string = input("Enter a String with combination of letters and digits:\n")

for i in string:
    if i >= '0' and i <= '9':
        digits += 1
    elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        letters +=1
        
print("String " +string+ " has %d digits and %d letters" %(digits, letters))

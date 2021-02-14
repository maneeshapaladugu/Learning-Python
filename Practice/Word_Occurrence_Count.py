#Python program to find the occurrence of a given word in a string
string = input("Enter a sequence of strings:\n")
word = input("Enter a word from the above sequence:\n")

strList = string.split(' ')
count = 0
for i in strList:
    if i == word:
        count += 1
print("Occurrences of word " + word + " is " + str(count))

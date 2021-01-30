message = 'It was a bright cold day in April, and the clocks were striking thirteen.'



count = {} #This dictionary will store the character key and its count. Ex: r:5

for character in message: #here, lower case and upper case counts are seperate
    count.setdefault(character, 0) #if character doesn't exists in count dictionary, sets the character count as 0 as an initialization
    count[character] = count[character] + 1

print(count)
#output:
#{'I': 1, 't': 6, ' ': 13, 'w': 2, 'a': 4, 's': 3, 'b': 1, 'r': 5, 'i': 6, 'g': 2, 'h': 3, 'c': 3, 'o': 2, 'l': 3, 'd': 3, 'y': 1, 'n': 4, 'A': 1, 'p': 1, ',': 1, 'e': 5, 'k': 2, '.': 1}

#-----------------------------------------------------------------------------------------------------

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} #This dictionary will store the character key and its count. Ex: r:5

for character in message.upper(): #returns an upper case from the string
    count.setdefault(character, 0) #if character doesn't exists in count dictionary, sets the character count as 0 as an initialization
    count[character] = count[character] + 1

print(count)
#output: All the lower cases are converted to upper case
#{'I': 7, 'T': 6, ' ': 13, 'W': 2, 'A': 5, 'S': 3, 'B': 1, 'R': 5, 'G': 2, 'H': 3, 'C': 3, 'O': 2, 'L': 3, 'D': 3, 'Y': 1, 'N': 4, 'P': 1, ',': 1, 'E': 5, 'K': 2, '.': 1}

#----------------------------------------------------
#The pprint() function in pprint module for a pretty print
import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {} #This dictionary will store the character key and its count. Ex: r:5

for character in message.upper(): #returns an upper case from the string
    count.setdefault(character, 0) #if character doesn't exists in count dictionary, sets the character count as 0 as an initialization
    count[character] = count[character] + 1

pprint.pprint(count)

#output:
{' ': 13,
 ',': 1,
 '.': 1,
 'A': 5,
 'B': 1,
 'C': 3,
 'D': 3,
 'E': 5,
 'G': 2,
 'H': 3,
 'I': 7,
 'K': 2,
 'L': 3,
 'N': 4,
 'O': 2,
 'P': 1,
 'R': 5,
 'S': 3,
 'T': 6,
 'W': 2,
 'Y': 1}





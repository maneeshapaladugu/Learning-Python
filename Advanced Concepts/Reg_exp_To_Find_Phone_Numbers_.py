import re  #Importing regular expression module to make of use of its methods

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #We create the regular expression objects using compile methos and we usually pass raw strings to compile() method
                                                      #We pass the text that defines the patterns that we are looking for
                                                      #\d is the regex for a numeric digital characters
mo = phoneNumRegex.search(message) # regex data type object has a search() method for searching a string and it returns a match object 
print(mo.group()) #Match object has a method group() that returns the pattern

#Output: 415-555-1011  #found the first occurrence of the pattern


########################################################################################################

#findall() method

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Call me at 415-555-1011 tomorrow, or at 415-555-9999'))

#Output: ['415-555-1011', '415-555-9999']

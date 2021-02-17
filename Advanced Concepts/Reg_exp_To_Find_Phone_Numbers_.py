import re  #Importing regular expression module to make of use of its methods

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #We usually pass raw strings to compile() method
                                                      #and we pass the text that defines the patterns that we are looking for
                                                      #\d is the regex for a numeric digital characters
mo = phoneNumRegex.search(message) # regex data type has a search() method Searching a message and it returns a match object 
print(mo.group()) #Match object has a method group() to tell you the actual string

#Output: 415-555-1011

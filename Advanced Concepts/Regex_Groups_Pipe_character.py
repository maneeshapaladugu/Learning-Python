Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import re
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneNumRegex.search('My number is 415-555-4242')
<re.Match object; span=(13, 25), match='415-555-4242'>
>>> #The regular expression object search() method returns a match object
>>> 
>>> #We would store that match object in a variable
>>> mo = phoneNumRegex.search('My number is 415-555-4242')
>>> mo.group()
'415-555-4242'
>>> #Match object has a group() method which would return the pattern
>>> 
>>> #########################################################################
>>> #Groups:
>>> 
>>> #We can use the paranthesis to mark out the groups
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> mp = phoneNumRegex.search('My number is 415-555-4242')
>>> mp.group()
'415-555-4242'
>>> mp.group(1)
'415'
>>> mo.group(2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    mo.group(2)
IndexError: no such group
>>> mp.group(2)
'555-4242'
>>> 

>>> phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')  #\( \)is used because we are literally looking for paranthesis
>>> mo = phoneNumRegex.search('My number is (415) 555-4242')
>>> mo.group()
'(415) 555-4242'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #################################################################3
>>> 
>>> #Pipe character
>>> 
>>> #We can also use pipe characters to match one or several patterns as part of your regular expression
>>> batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group()
'Batmobile'
>>> #The pattern the we were looking for is the bat followed by bunch of possible suffixes like man, mobile, copter, bat
>>> 
>>> 
>>> mo = batRegex.search('Batmotorcycle lost a wheel') #if the search() method can't find that regular expression pattern in the string you passed, its going to return None
>>> 
>>> mo == None
True
>>> # if you just go and blindly call group() on match object, its going to throw error
>>> 
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
>>> mo = batRegex.search('Batmobile lost a wheel')
>>> mo.group(1)
'mobile'
>>> 
>>> mo = batRegex.search('Batman lost a wheel')
>>> mo.group(1)
'man'
>>> 
>>> mo = batRegex.search('Batbat lost a wheel')
>>> mo.group(1)
'bat'
>>> #As we can pass the bunch of possible suffixes in a group, if we want to find out which suffix that was found in the pattern, we can use group(1)
>>> 
>>> #Recap:
>>> >>> #Groups are crated in regex strings with paranthesis
>>> #The first set of paranthesis is group 1, the second is 2 and so on.
>>> #Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string and so on
>>> #use \(and\) to match literal paranthesis in the regex string
>>> #The | pipe can match one of many possible groups

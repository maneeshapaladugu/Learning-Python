Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String methods:
>>> #Unlike list methods, string methods return a new string value rather than modifying string in place,
#Since strings are immutable, its not possible to modify the strings in place
>>> 
>>> 
>>> spam = 'Hello world!'
>>> spam
'Hello world!'
>>> spam.upper()
'HELLO WORLD!'
>>> spam.lower()
'hello world!'
>>> spam
'Hello world!' #if you observe here, spam has not been changed
>>> 
>>> answer = input()
yes #here it waits for user input
>>> answer
'yes'
>>> answer = input()
YES#storing upper case
>>> answer
'YES'

>>> if answer == 'yes':
	print('Playing again')

	
>>> answer == 'yes'
False
>>> answer.lower() == 'yes'
True
>>> answer = 'yEs'
>>> answer
'yEs'
>>> answer.lower() == 'yes'
True
>>> 
>>> if answer == 'yes':
	print('Playing again')

	
>>> if answer.lower() == 'yes':
	print('Playing again')

#Output:	
Playing again
>>> 


>>> answer = input()
yes
>>> if answer.upper() == 'YES':
	print('Playing again')

#Output:	
Playing again

>>> 
>>> 
>>> #string methods isupper() and islower() returns the boolean value
>>> spam = 'Hello World!'
>>> spam.islower()
False
>>> spam.isupper()
False
>>> spam = 'hello world!'
>>> spam.islower()
True
>>> spam = 'HELLO WORLD!'
>>> spam.isupper()
True
>>> spam = ''
>>> spam.isupper()
False
>>> spam.islower()
False
>>> '12345'.islower()
False
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().isupper()
True
>>> 
>>> 
>>> spam = 'Hello world!'

>>> spam.isalpha()
False
>>> spam = 'Hello'
>>> spam.isalpha()
True
>>> spam = 'Hello 123'
>>> spam.isalnum()
False
>>> spam = 'Hello123'
>>> spam.isalnum()
True
>>> spam = '123'
>>> spam.isdecimal()
True
>>> spam = '12.6'
>>> spam.isdecimal()
False
>>> spam.isspace()
False
>>> spam = ''
>>> spam.isspace()
False
>>> spam = ' '
>>> spam.isspace()
True
>>> #istitle() - returns true for a title case
>>> spam = 'Hello World'
>>> spam.istitle()
True
>>> spam = 'hello world'
>>> spam.istitle()
False

>>> 
>>> 
>>> 'Hello world'.isspace()
False
>>> 'Hello world'[5].isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'hello world'.title() #returns a Title Case string
'Hello World'
>>> 
>>> 
>>> 'Hello world'.startswith('Hello')
True
>>> 'Hello world'.startswith('H')
True
>>> 'Hello world'.startswith('ello')
False
>>> 'Hello world'.endswith('world')
True
>>> 'Hello world'.endswith('worl')
False
>>> 
>>> 
>>> 
>>> #join() method: when we have a list of strings that needs to be joined together in to a single string,
#On passing the list of strings, join() returns a single string
>>> 
>>> ','.join(['cats','rats','bats'])
'cats,rats,bats'
>>> ''.join(['cats','rats','bats'])
'catsratsbats'
>>> ' '.join(['cats','rats','bats'])
'cats rats bats'
>>> '\n\n'.join(['cats','rats','bats'])
'cats\n\nrats\n\nbats'
>>> print('\n\n'.join(['cats','rats','bats']))
cats

rats

bats
>>> 
>>> 
>>> #split() method: It does the opposite to join() method. Its called on a single string value and returns a list of strings
>>> 
>>> 'My name is Simon'.split()
['My', 'name', 'is', 'Simon']
>>> 'My name is Simon'.split('m')
['My na', 'e is Si', 'on']
>>> 
>>> 
>>> 
>>> 'Hello'.rjust(10)
'     Hello'
>>> len('     Hello')
10
>>> 'Hello'.ljust(10)
'Hello     '
>>> 'Hello'.ljust(20)
'Hello               '
>>> 'Hello'. rjust(20, '*') #Hello to be right justified along with * instead of spaces
'***************Hello'
>>>  
>>> 'Hello'.ljust(25, '-')
'Hello--------------------'
>>> 'Hello'.center(20)
'       Hello        '
>>> 'Hello'.center(20, '=')
'=======Hello========'
>>> name = 'Maneesha'
>>> name.center(20, '=')
'======Maneesha======'
>>> name = 'Maneesha Paladugu'
>>> name.center(20, '=')
'=Maneesha Paladugu=='
>>> 
>>> 
>>> 
>>> 'Hello'.rjust(10)
'     Hello'
>>> spam = 'Hello'.rjust(10)
>>> #strip() method removes the whitespaces and returns a new string. Original string is not modified
>>> spam.strip()
'Hello'

>>> spam
'     Hello'
>>> #lstrip(), rstrip() - left strip and right strip
#strip() - strip both left and right
>>> spam = spam.strip()
>>> spam
'Hello'
>>> '    x    '.strip()
'x'
>>> '    x    '.lstrip()
'x    '
>>> '    x    '.rstrip()
'    x'

>>> #we can pass strip() method a string with characters to strip instead of whitespaces
>>> 
>>> 'ManeeshaManeeshaManManeeManEESHA'.strip('ee')
'ManeeshaManeeshaManManeeManEESHA'
>>> 'ManeeshaManeeshaManManeeManEESHA'.strip('Man')
'eeshaManeeshaManManeeManEESHA'
>>> 'ManeeshaManeeshaManManeeManEESHA'.strip('aee')
'ManeeshaManeeshaManManeeManEESHA'
>>> 'ManeeshaManeeshaManManeeManEESHA'.strip('ne')
'ManeeshaManeeshaManManeeManEESHA'
>>> 'ManeeshaManeeshaManManeeManEESHA'.strip('Me')
'aneeshaManeeshaManManeeManEESHA'
>>> 'ManeeshaManeeshaManManeeMan'.strip('Man')
'eeshaManeeshaManManee'
>>> 'ManeeshaManeeshaManManeeMan'.strip('anM')
'eeshaManeeshaManManee'
>>> 
>>> 
>>> 
>>> spam = 'Hello there!'
>>> spam.replace('e','XYZ')
'HXYZllo thXYZrXYZ!'
>>> 
>>> >>> #paste() method paste the string values that is already copied to clipboard
>>> import pyperclip
>>> pyperclip.copy('Hello!!!!!!')
>>> pyperclip.paste()
'Hello!!!!!!'

>>> 

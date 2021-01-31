Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 'Hello'
'Hello'
>>> 'That is Alice's cat'
SyntaxError: invalid syntax
>>> "That is Alice's cat" #Now, Python understands that ' is not end of the string
"That is Alice's cat"
>>> 'Say Hi to Alice\'s mother' #using escape character \'
"Say Hi to Alice's mother"
>>> 
>>> #Escape characters:
>>> #single quote \'
>>> #double quote \"
>>> #tab \t
>>> #new line \n
>>> #blackslash \\ 
>>> 
>>> 
>>> print('Hello there!\nHow are you?\nI\'m fine')
Hello there!
How are you?
I'm fine
>>> 
>>> 
>>> #Raw strings: Raw strings helps us in treating backslash as a normal character.
>>> r'Hello'
'Hello'
>>> r'That is Carol\'s cat'
"That is Carol\\'s cat"
>>> #Don’t get confused with the output having two backslashes. It’s just to show it as a normal python string where backslash is being escaped
>>> 
>>> r'\''
"\\'"
>>> 
>>> 
>>> 
>>> print(r'\'')
\'
>>> print(r'That is Carol\'s cat')
That is Carol\'s cat
>>> 
>>> 
>>> print('Hi\xHello')#normal string
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \xXX escape

>>> print(r'Hi\xHello')#raw string
Hi\xHello
>>> print(r'Hi\nHello')#raw string
Hi\nHello
>>> 

>>> #Some of the invalid raw strings are:
>>> #r'\'  # missing end quote because the end quote is being escaped
>>> #r'ab\\\'  # first two backslashes will escape each other, the third one will try to escape the end quote
>>> 
>>> #Let’s look at some of the valid raw string examples with quotes
>>> print(r'\'')
\'
>>> print(r'ab\\')
ab\\

>>> print(R'\\\"')
\\\"
>>> 
>>> #Let's look at the output of invalid raw strings:
>>> print(r'\')
      
SyntaxError: EOL while scanning string literal
>>> print(r'ab\\\')
      
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #Multiline strings with triple quotes:
>>> #Multiline strings starts and ends with ''' or """
>>> #tabs or new lines in between the strings are considered as part of the string

>>> print("""Dear Alice,
Congratulations for winning the competetion. Happy to hear this!
Thanks,
Joe""")
Dear Alice,
Congratulations for winning the competetion. Happy to hear this!
Thanks,
Joe
>>> 
>>> spam = """Dear Alice,
Congratulations for winning the competetion. Happy to hear this!
Thanks,
Joe"""
>>> 
>>> spam
'Dear Alice,\nCongratulations for winning the competetion. Happy to hear this!\nThanks,\nJoe'
>>> 

>>> 

>>> #Similarities between strings and lists:
>>> 'Hello world!' #within single quotes
'Hello world!'
>>> "Hello world!" #within double quotes
'Hello world!'
>>> spam = 'Hello world!'
>>> spam
'Hello world!'
>>> spam[0]
'H'
>>> spam[-1]
'!'
>>> 'Hello' in spam
True
>>> 'x' in spam
False
>>> 'HELLO' in spam
False
>>> spam[1:5]
'ello'
>>> 

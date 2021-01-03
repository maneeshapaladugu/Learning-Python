Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
>>> 
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
>>> spam[0]
'cat'
>>> spam[1]
'bat'
>>> spam[2]
'rat'
>>> spam[3]
'elephant'
>>> spam[4]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    spam[4]
IndexError: list index out of range
>>> 
>>> spam = [['cat', 'bat'],[10, 20, 30, 40, 50]]
>>> spam
[['cat', 'bat'], [10, 20, 30, 40, 50]]
>>> 
>>> spam[0]
['cat', 'bat']
>>> spam[1]
[10, 20, 30, 40, 50]
>>> spam[0][1]
'bat'
>>> spam[0][0]
'cat'
>>> spam[1][0]
10
>>> spam[2][0]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    spam[2][0]
IndexError: list index out of range
>>> spam [1][1]
20
>>> spam[1][2]
30
>>> spam[1][3]
40
>>> spam[1][4]
50
>>> 
>>> spam = [['cat', 'bat'], 10, 20, 30]
>>> 
>>> spam
[['cat', 'bat'], 10, 20, 30]
>>> 
>>> spam[1]
10
>>> spam[0]
['cat', 'bat']
>>> spam[0][1]
'bat'
>>> spam[0][0]
'cat'
>>> spam[3]
30
>>> 
>>> 
>>> spam = ['cat', 'bat', 'rat', 'elephant']
>>> spam
['cat', 'bat', 'rat', 'elephant']
>>> spam[-1]
'elephant'
>>> spam[-2]
'rat'
>>> spam[-3]
'bat'
>>> spam[-4]
'cat'
>>> spam[-5]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    spam[-5]
IndexError: list index out of range
>>> 
>>> 
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] +
SyntaxError: invalid syntax
>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3]
'The elephant is afraid of the bat'
>>> 
>>> 
>>> 
>>> spam[1:3]
['bat', 'rat']
>>> #the above slice spam[1:3] evaluates to a new value
>>> 
>>> 
>>> spam = 'Hello'
>>> spam
'Hello'
>>> spam = [10, 20, 30]
>>> spam[1] = 'Hello'
>>> spam
[10, 'Hello', 30]
>>> spam[1:3] = ['CAT', 'DOG', 'ELEPHANT']
>>> spam
[10, 'CAT', 'DOG', 'ELEPHANT']
>>> spam[:2]#starts with 0 by default
[10, 'CAT']
>>> spam[1:]#ends with n by default
['CAT', 'DOG', 'ELEPHANT']
>>> 
>>> 
>>> del spam[2]
>>> spam
[10, 'CAT', 'ELEPHANT']
>>> del spam[2]
>>> spam
[10, 'CAT']
>>> 
>>> 
>>> 
>>> 
>>> len('Hello')
5
>>> len([1,2,3])#length of list
3
>>> 
>>> 'Hello' + 'world'
'Helloworld'
>>> 
>>> [1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
>>> 
>>> 'Hello' * 3
'HelloHelloHello'
>>> [1,2,3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> int('42')
42
>>> str(43)
'43'
>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> 'how' in ['Hello', 'Hi', 'Hey', 'How']
False
>>> How in ['Hello', 'Hi', 'Hey', 'How']
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    How in ['Hello', 'Hi', 'Hey', 'How']
NameError: name 'How' is not defined
>>> 'How' in ['Hello', 'Hi', 'Hey', 'How']
True
>>> 
>>> 'how' not in ['Hello', 'Hi', 'Hey', 'How']
True
>>> 
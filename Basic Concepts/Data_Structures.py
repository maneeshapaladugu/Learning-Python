Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List of Dictionaries is called Data Structures
>>> cat = {'name': 'Zophie', 'age':7, 'color': 'grey'}
>>> cat
{'name': 'Zophie', 'age': 7, 'color': 'grey'}
>>> allcats = []
>>> allcats
[]
>>> allcats.append({'name': 'Zophie', 'age':7, 'color': 'grey'})
>>> allcats.append({'name': 'Jony', 'age':5, 'color': 'black'})
>>> allcats.append({'name': 'Fat-tail', 'age':5, 'color': 'grey'})
>>> allcats.append({'name': '???', 'age':-1, 'color': 'orange'})
>>> allcats
[{'name': 'Zophie', 'age': 7, 'color': 'grey'}, {'name': 'Jony', 'age': 5, 'color': 'black'}, {'name': 'Fat-tail', 'age': 5, 'color': 'grey'}, {'name': '???', 'age': -1, 'color': 'orange'}]
>>> 
>>> 

>>> theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> 
>>> theBoard
{'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
>>> import pprint
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': ' ',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> 
>>> 
>>> theBoard['mid-M'] = 'X'
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': ' ',
 'mid-L': ' ',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': ' ',
 'top-M': ' ',
 'top-R': ' '}
>>> 
>>> 
>>> theBoard['top-L'] = 'o'
>>> theBoard['top-M'] = 'o'
>>> theBoard['top-R'] = 'o'
>>> 
>>> theBoard['mid-L'] = 'x'
>>> theBoard['low-R'] = 'x'
>>> 
>>> pprint.pprint(theBoard)
{'low-L': ' ',
 'low-M': ' ',
 'low-R': 'x',
 'mid-L': 'x',
 'mid-M': 'X',
 'mid-R': ' ',
 'top-L': 'o',
 'top-M': 'o',
 'top-R': 'o'}
>>> 
>>> 

>>> 
>>> def printBoard(board): 
	print(board['top-L'] +  '|' + board['top-M'] + '|' + board['top-R'])
	print('-----')
	print(board['mid-L'] +  '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----')
	print(board['low-L'] +  '|' + board['low-M'] + '|' + board['low-R'])

	
>>> printBoard(theBoard)
o|o|o
-----
x|X| 
-----
 | |x
>>> 
>>> 
>>> 
>>> #type function to know the data type of a value
>>> type(42)
<class 'int'>
>>> type('hello')
<class 'str'>
>>> type(3.14)
<class 'float'>
>>> type(theBoard)
<class 'dict'>
>>> type(theBoard['top-R'])
<class 'str'>
>>> 

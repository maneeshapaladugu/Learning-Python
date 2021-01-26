Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


>>> #Like a list, a dictionary is a collection of many values
>>> #But unlike list indexes, dictionaries indexes can use many differential types
>>> #Dictionaries indexes are called keys
>>> #Dictionaries index with its associated value is called key value pair
>>> #A key value pair is called as item
>>> 
>>> myCat = {'size':'fat', 'color':'grey', 'disposition':'loud'}
>>> myCat
{'size': 'fat', 'color': 'grey', 'disposition': 'loud'}

>>> myCat['size']
'fat'
>>> 
>>> 
>>> 'My cat has ' + myCat['color'] + ' tail'
'My cat has grey tail'
>>>

#*******************************************************************************************************************

>>> 
>>> #Lists can have integer indexes only, which starts with 0 by default
>>> #Dictionaries can have integer indexes but they do not have to start with 0
>>> spam = {12345:'Luggage combination', 42:'The answer'}
>>> 
>>> #unlike lists, the items in dictionaries are unordered
>>> spam[0]#Error
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    spam[0]
KeyError: 0

>>> spam[12345]
'Luggage combination'
>>> spam[42]
'The answer'
>>>

#*******************************************************************************************************************
>>> 
>>> [1,2,3] == [3,2,1] #Though contents are same, order is different here and thus these lists are not equal
False
>>> 
>>> eggs = {'name':'Zophie', 'species':'cat', 'age':8}
>>> ham = {'species':'cat', 'name':'Zophie', 'age':8}
>>> eggs == ham
True
>>> #Unlike lists, while comparing dictionaries, order is not important
>>> 

>>> 'color' in eggs #using 'in' operator to check if a key exists in a dictionary or not#Should provide keys, not values
False
>>> 'name' in eggs
True
>>> 'name' not in eggs
False
>>> 
>>> #*******************************************************************************************************************

>>> #Dictionaries are mutable like lists
>>> #Variables hold references to dictionary values 
>>> #Dictionary methods: keys(), values(), items():
>>> list(eggs.keys())
['name', 'species', 'age']
>>> list(eggs.values())
['Zophie', 'cat', 8]
>>> list(eggs.items())
[('name', 'Zophie'), ('species', 'cat'), ('age', 8)]
>>> 
>>> 
>>> eggs.keys()
dict_keys(['name', 'species', 'age'])

>>> for k in eggs.keys():
	print(k)

#Output:	
name
species
age
>>> 
>>> 
>>> for v in eggs.values():
	print(v)

#Output:	
Zophie
cat
8
>>> 

>>> for m,n in eggs.items():
	print(m,n)

#Output:	
name Zophie
species cat
age 8
>>> 
>>> 
>>> for i in eggs.items():
	print(i)

#Output:	
('name', 'Zophie')
('species', 'cat')
('age', 8)
>>> 
>>>

#*******************************************************************************************************************

>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> 
>>> 'cat' in eggs.values()
True
>>> 
>>> 
>>> eggs['color']
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    eggs['color']
KeyError: 'color'
>>> 
>>> if 'color' in eggs:  #to avoid above error
	print(eggs['color'])

	
>>> if 'name' in eggs:
	print(eggs['name'])

#Output:	
Zophie
>>>

#*******************************************************************************************************************

>>> 
>>> #Alternate to 'in' operator in above case: using get() method
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.get('age', 0) #2nd arg specifies the default value to be returned if key doesn't exists in dictionary
8
>>> 
>>> eggs.get('color','')#Return blank string if color key doesn't exists
''

>>> picnicItems = {'apples':5, 'cups':2}
>>> print('I am bringing ' + str(picnicItems.get('napkins',0)) + ' napkins to the picnic')
I am bringing 0 napkins to the picnic
>>> 
>>> 
>>> print('I am bringing ' + str(picnicItems['napkins']) + ' napkins to the picnic')#Error
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    print('I am bringing ' + str(picnicItems['napkins']) + ' napkins to the picnic')
KeyError: 'napkins'
>>> 
>>> 
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> if 'color' not in eggs:
	eggs['color'] = 'black'

	
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
>>> 
>>>

#*******************************************************************************************************************

>>> #Alternate to above if condition:
>>> 
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8}
>>> eggs.setdefault('color', 'black')
'black'
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
>>> eggs.setdefault('color', 'orange')
'black'
>>> eggs
{'name': 'Zophie', 'species': 'cat', 'age': 8, 'color': 'black'}
>>> #setdefault sets key value pair only if a key doesn't exists in given dictionary 
>>> 

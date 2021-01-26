Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#Each data type has its own set of methods
#following are the methods of list datatype
#1.index()
#2.append()
#3.insert()
#4.remove()
#5.sort()

>>> spam = ['hello', 'hi', 'hey', 'how']
>>> spam.index('hello')#The index() List method returns the index of value passed to it
0

>>> index('hello')#Error
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    index('hello')
NameError: name 'index' is not defined
>>>

>>> spam.index('how') 
3

>>> spam.index('dfadfasfdadfasfd')#Error
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    spam.index('dfadfasfdadfasfd')
ValueError: 'dfadfasfdadfasfd' is not in list
>>> 
>>> 
>>> spam = ['cat', 'dog', 'bat']
>>> spam
['cat', 'dog', 'bat']

>>> spam.append('mouse')
>>> spam
['cat', 'dog', 'bat', 'mouse']

>>> 
>>> spam.insert(1, 'parrot')
>>> spam
['cat', 'parrot', 'dog', 'bat', 'mouse']
>>> 
>>> 
>>> spam.append('sparrow')
>>> spam.append('sparrow')
>>> spam.append('sparrow')
>>> spam.append('sparrow')
>>> spam
['cat', 'parrot', 'dog', 'bat', 'mouse', 'sparrow', 'sparrow', 'sparrow', 'sparrow']
>>> 
>>> 
>>> eggs = 'hello'
>>> eggs.append('world')#Error
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    eggs.append('world')
AttributeError: 'str' object has no attribute 'append'
>>> 
>>> 
>>> 
>>> spam = ['cat', 'rat', 'bat', 'mat']
>>> spam
['cat', 'rat', 'bat', 'mat']

>>> spam.remove('bat')
>>> spam
['cat', 'rat', 'mat']

>>> spam.remove('bat')#Error
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    spam.remove('bat')
ValueError: list.remove(x): x not in list
>>> 
>>> 
>>> 
>>> del spam[0]
>>> spam
['rat', 'mat']
>>> 
>>> 
>>> 
>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
>>> spam.remove('cat')#Each time it removes the first occurrence
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
>>> 
>>> 
>>> 

>>> spam = [2,5,3.14,1,-7]
>>> spam
[2, 5, 3.14, 1, -7]

>>> spam.sort()#The sort() method sorts the list ascending by default
>>> spam
[-7, 1, 2, 3.14, 5]
>>> 
>>> 
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam
['ants', 'cats', 'dogs', 'badgers', 'elephants']

>>> spam.sort()#Reverse parameter is optional and false by default
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

>>> spam.sort(reverse=True)
>>> spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

>>> spam.sort(reverse=False)
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']

>>> 
>>> spam = [1,2,3,'Alice', 'Bob']
>>> spam.sort()#Error
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> 
>>> 
>>> spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol',  'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> 
>>> 

>>> spam = ['a', 'B', 'A', 'b']
>>> spam.sort() 
>>> spam
['A', 'B', 'a', 'b']
>>> 
>>> 
 

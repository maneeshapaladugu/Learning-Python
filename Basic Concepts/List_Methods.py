Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> spam = ['hello', 'hi', 'hey', 'how']
>>> spam.index('hello')
0
>>> index('hello')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    index('hello')
NameError: name 'index' is not defined
>>> 
>>> spam.index('how') #The index() List method...retunrs the index of value passed... each data type has its own set of methods
3
>>> spam.index('dfadfasfdadfasfd')
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
>>> eggs.append('world')
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
>>> spam.remove('bat')
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
>>> spam.remove('cat')
>>> spam
['bat', 'rat', 'cat', 'hat', 'cat']
>>> 
>>> 
>>> 
>>> spam = [2,5,3.14.1.-7]
SyntaxError: invalid syntax
>>> spam = [2,5,3.14,1,-7]
>>> spam
[2, 5, 3.14, 1, -7]
>>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> 
>>> 
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam
['ants', 'cats', 'dogs', 'badgers', 'elephants']
>>> spam.sort()
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
>>> spam.sort()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    spam.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> 
>>> 
>>> spam = ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> 
>>> 
>>> spam = ['Alice', 'Bob', 'ants', 'badgers', 'Carol',  'cats']
>>> spam.sort()
>>> spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
>>> 
>>> 
>>> spam = ['a', 'Z', 'A', 'Z']
>>> spam.sort()
>>> spam
['A', 'Z', 'Z', 'a']
>>> spam = ['a', 'B', 'A', 'b']
>>> spam.sort()
>>> spam
['A', 'B', 'a', 'b']
>>> 
>>> 
>>> spam = ['a', 'B', 'A', 'b']
>>> spam
['a', 'B', 'A', 'b']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'B', 'b']
>>> spam.sort(key=str.lower)
>>> spam
['a', 'A', 'B', 'b']
>>> 
>>> 
>>> spam = ['a', 'z', 'A', 'Z']
>>> spam.sort()
>>> spam
['A', 'Z', 'a', 'z']
>>> spam.sort(key=str.lower)
>>> spam
['A', 'a', 'Z', 'z']
>>> 
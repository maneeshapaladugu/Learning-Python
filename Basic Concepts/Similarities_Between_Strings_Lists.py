>>> list('Hello')
['H', 'e', 'l', 'l', 'o']
>>> name = 'Maneesha'
>>> name[0]
'M'
>>> name[1]
'a'
>>> name[2]
'n'
>>> name[-1]
'a'
>>> name[1:3]
'an'
>>> 'ee' in name
True
>>> 'she' in name
False
>>> for letter in name:
	print(letter)

	
M
a
n
e
e
s
h
a
>>> 
>>>  #mutable and immutable datatypes
>>> #list is mutable -it can be changes
>>> #*changed
>>> #string value is immutable - it can not be changed
>>> 
>>> name = 'Zophie the cat'
>>> name[7]
't'
>>> name[7] = 'm'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name[7] = 'm'
TypeError: 'str' object does not support item assignment
>>> 
>>> 
>>> 
>>> newName = name[0:7] + 'the' + name[8:12]
>>> newName
'Zophie thehe c'
>>> 
>>> newName = name[0:7] + 'a' + name[10:14]
>>> newName
'Zophie a cat'
>>> 
>>> 

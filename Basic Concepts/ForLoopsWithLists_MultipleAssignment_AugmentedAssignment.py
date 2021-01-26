Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> for i in range(4):
	print(i)

#Output:	
0
1
2
3

>>> range(4)
range(0, 4)

>>> [0,1,2,3] #range object is similar to the list
[0, 1, 2, 3]
>>> 
>>> for i in [0,1,2,3]: # list can also be used in place of range object
	print(i)

#Output:
0
1
2
3

>>> range(4)
range(0, 4)
>>> list(range(4))
[0, 1, 2, 3]

>>> list(range(0,100,2)) #step twice from 0 to 99
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
>>>

>>> spam = list(range(0,100,3))#step thrice from 0 to 99 and assign the list to spam

>>> spam
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
>>> 
>>> 
>>> supplies = ['pens', 'staplers', 'binders', 'pins']
>>> 
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' +supplies[i])

#Output:	
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: binders
Index 3 in supplies is: pins
>>> 
>>> 
>>> supplies = ['pens', 'pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens','pens']
>>> 
>>> for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' +supplies[i])

#Output:	
Index 0 in supplies is: pens
Index 1 in supplies is: pens
Index 2 in supplies is: pens
Index 3 in supplies is: pens
Index 4 in supplies is: pens
Index 5 in supplies is: pens
Index 6 in supplies is: pens
Index 7 in supplies is: pens
Index 8 in supplies is: pens
Index 9 in supplies is: pens
Index 10 in supplies is: pens
Index 11 in supplies is: pens
Index 12 in supplies is: pens
Index 13 in supplies is: pens
Index 14 in supplies is: pens
Index 15 in supplies is: pens
Index 16 in supplies is: pens
Index 17 in supplies is: pens
Index 18 in supplies is: pens
Index 19 in supplies is: pens
Index 20 in supplies is: pens
Index 21 in supplies is: pens
Index 22 in supplies is: pens
Index 23 in supplies is: pens
Index 24 in supplies is: pens
Index 25 in supplies is: pens
Index 26 in supplies is: pens
Index 27 in supplies is: pens
Index 28 in supplies is: pens
>>> 
>>> 
>>> 
>>> cat = ['fat', 'orange', 'loud']
>>> size = cat[0]
>>> color = cat[1]
>>> disposition = cat[2]
>>> 
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'
>>> 
>>> 
>>> 
>>> size, color, disposition = cat #multiple assignment trick
>>> 
>>> size
'fat'
>>> color
'orange'
>>> disposition
'loud'
>>> 
>>> 
>>> size, color, disposition = 'skinny', 'black', 'quiet'
>>> size
'skinny'
>>> color
'black'
>>> disposition
'quiet'
>>> 
>>> 
>>> 
>>> a = 'AAA'
>>> b = 'BBB'
>>> a, b = b, a #swap/multiple assignemnt
>>> a
'BBB'
>>> b
'AAA'
>>> 
>>> #Augmented assignment operators:
>>> 
>>> spam = 42
>>> spam = spam + 1 #common operation
>>> spam += 1 #Augmented assignment operation
>>> spam
44
>>> 

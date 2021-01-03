Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> #The difference between mutable and immutable comes up with "references"
>>> 
>>> spam = 42
>>> spam
42
>>> cheese = spam
>>> cheese
42
>>> spam = 100
>>> spam
100
>>> cheese
42
>>> 
>>> 
>>> 
>>> 
>>> 
>>> spam = [0,1,2,3,4,5]
>>> cheese = spam
>>> cheese
[0, 1, 2, 3, 4, 5]
>>> spam
[0, 1, 2, 3, 4, 5]
>>> cheese[1] = 'Hello!'
>>> cheese
[0, 'Hello!', 2, 3, 4, 5]
>>> spam
[0, 'Hello!', 2, 3, 4, 5]
>>> #Here spam also got modified when cheese got changed
>>> #why spam has been changed? Because both cheese and spam are referencing the same list [0,1,2,3,4,5]
>>> #in spam, a reference to list is stored,not the actual list
>>> #when spam has been copied in to cheese, a copy of same reference id has been stored in cheese
>>> #in turn both spam and cheese are pointing to the same memory location (list)
>>> 
>>> 
>>> #immutable values don't have this problems because they can't be modified "in place". They can only be replaced by new values
>>> 
>>> 
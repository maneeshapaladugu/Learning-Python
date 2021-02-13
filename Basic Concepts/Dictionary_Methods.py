Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Dictionary copy() method - This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
>>> original = {1:'one', 2: 'two'}
>>> new =original.copy()
>>> print('Original:', original)
Original: {1: 'one', 2: 'two'}
>>> print('New',new)
New {1: 'one', 2: 'two'}
>>> 
>>> 
>>> 
>>> #Difference in Using copy() method, and = Operator to Copy Dictionaries - When copy() method is used, a new dictionary is created which is filled with a copy of the
#references from the original dictionary. 

>>> original = {1:'one', 2:'two'}
>>> new = original
>>> new.clear() #removing all elements from the list
>>> print('new:',new)
new: {}
>>> print('original:', original)
original: {}
>>> #Here, when new dictionary is cleared, original dictionary is also cleared.
>>> 
>>> 
>>> 
>>> 
>>> original = {1:'one',2:'two'}
>>> new = original.copy()
>>> new.clear() #removing all elements from the list
>>> print('New:',new)
New: {}
>>> print('Original:',original)
Original: {1: 'one', 2: 'two'}
>>> #Here, when new dictionary is cleared, original dictionary remains unchanged.
>>> #######################################################
>>> 
>>> 
>>> #The dictionary fromkeys() method - The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided by the user.#Dictionary copy() method - This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
>>> 
>>> 
>>> keys = {'a','e','i','o','u'}
>>> vowels = dict.fromkeys(keys)
>>> print(vowels)
{'a': None, 'e': None, 'i': None, 'u': None, 'o': None}
>>> 
>>> 
>>> 
>>> keys = {'a','e','i','o','u'}
>>> value = 'vowel'
>>> vowels = dict.fromkeys(keys,value)
>>> print(vowels)
{'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'u': 'vowel', 'o': 'vowel'}
>>> 
>>> 
>>> 
>>> #Create a dictionary from a mutable object list
>>> keys = {'a','e','i','o','u'}
>>> value = [1]
>>> 
>>> vowels = dict.fromkeys(keys,value)
>>> print(vowels)
{'a': [1], 'e': [1], 'i': [1], 'u': [1], 'o': [1]}
>>> value.append(2)#updating the value
>>> print(vowels)
{'a': [1, 2], 'e': [1, 2], 'i': [1, 2], 'u': [1, 2], 'o': [1, 2]}
>>> #If value is a mutable object (whose value can be modified) like list, dictionary, etc., when the mutable object is modified, each element of the sequence also gets updated.
>>> 
>>> #This is because each element is assigned a reference to the same object (points to the same object in the memory).
>>> 
>>> #To avoid this issue, we use dictionary comprehension.
>>> 
>>> keys = {'a','e','i','o','u'}
>>> value = [1]
>>> vowels = {key:list(value) for key in keys}# you can alse use {key:value[:] for key in keys}
>>> print(vowels)
{'a': [1], 'e': [1], 'i': [1], 'u': [1], 'o': [1]}
>>> value.append(2) #updating the value
>>> print(vowels)
{'a': [1], 'e': [1], 'i': [1], 'u': [1], 'o': [1]}
>>> 
>>> 
>>> ###################################################################################
>>> #Dictionary get() method - The get() method returns the value for the specified key if key is in dictionary.
>>> person = {'name':'Maneesha',age:24}
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    person = {'name':'Maneesha',age:24}
NameError: name 'age' is not defined
>>> person = {'name':'Maneesha','age'4:24}
SyntaxError: invalid syntax
>>> person = {'name':'Maneesha','age':24}
>>> 
>>> print('Name: ', person.get('name'))
Name:  Maneesha
>>> print('Age: ', person.get('age'))
Age:  24
>>> print('Salary: ',person.get('salary'))#Returns None if the key is not found and value is not specified.
Salary:  None
>>> print('Salary: ',person.get('salary'), 0.0)#Returns value if the key is not found and value is specified.

Salary:  None 0.0
>>> 
>>> 
>>> #get() method returns a default value if the key is missing.
>>> #However, if the key is not found when you use dict[key], KeyError exception is raised.
>>> 
>>> person={}
>>> print('salary: ',person.get('salary'))
salary:  None
>>> print(person['salary'])
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(person['salary'])
KeyError: 'salary'
>>> 
>>> 
>>> ####################################################################################
>>> #Python Dictionary items() - The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.
>>> #items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
>>> 
>>> sales = {'apple':2, 'orange':3,'grapes':4}
>>> print(sales.items())
dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
>>> 
>>> 
>>> sales = {'apple':2, 'orange':3,'grapes':4}
>>> items = sales.items()
>>> print('Original items: ',items)
Original items:  dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])
>>> del[sales['apple']]
>>> print('Updated items: ',items)
Updated items:  dict_items([('orange', 3), ('grapes', 4)])
>>> #The view object items doesn't itself return a list of sales items but it returns a view of sales's (key, value) pair.If the list is updated at any time, the changes are reflected on the view object itself, as shown in the above program.
>>> #########################################################
>>> 
>>> 
>>> #Python Dictionary keys() - The keys() method returns a view object that displays a list of all the keys in the dictionary
>>> #When the dictionary is changed, the view object also reflects these changes.
>>> person = {'name': 'Maneesha','age':24}
>>> print(person.keys())
dict_keys(['name', 'age'])
>>> empty_dict={}
>>> print(empty_dict.keys())
dict_keys([])
>>> 
>>> 
>>> 
>>> #How keys() works when dictionary is updated?
>>> person={'name': 'Maneesha','age':24}
>>> keys = person.keys()
>>> print(keys)
dict_keys(['name', 'age'])
>>> 
>>> person.update({'Course':'Python'})
>>> print(keys)
dict_keys(['name', 'age', 'Course'])
>>> print(person)
{'name': 'Maneesha', 'age': 24, 'Course': 'Python'}
>>> 
>>> ############################################################
>>> 
>>> #Python Dictionary popitem() - The Python popitem() method removes and returns the last element (key, value) pair inserted into the dictionary.
>>> person = {'name':'Maneesha','age':24,'course':'Python'}
>>> result = person.popotem()
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    result = person.popotem()
AttributeError: 'dict' object has no attribute 'popotem'
>>> result = person.popitem()
>>> print(result)
('course', 'Python')
>>> print(person)
{'name': 'Maneesha', 'age': 24}
>>> person['Profession'] = 'Plumber'
>>> person
{'name': 'Maneesha', 'age': 24, 'Profession': 'Plumber'}
>>> result = person.popitem()
>>> print(result)
('Profession', 'Plumber')
>>> print(person)
{'name': 'Maneesha', 'age': 24}
>>> 
>>> ###########################################################
>>> #Python Dictionary setdefault() - The setdefault() method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
>>> 
>>> #How setdefault() works when key is in the dictionary?
>>> 
>>> person = {'name':'Maneesha','age':24}
>>> age = person.setdefault('age')
>>> print('person: ',person)
person:  {'name': 'Maneesha', 'age': 24}
>>> print('Age:' ,age)
Age: 24
>>> 
>>> #How setdefault() works when key is not in the dictionary?
>>> person = {'name':'Maneesha'}
>>> salary = person.setdefault('salary')
>>> print(person)
{'name': 'Maneesha', 'salary': None}
>>> print(salary)
None
>>> 
>>> age=person.setdefault('age',22)
>>> print(person)
{'name': 'Maneesha', 'salary': None, 'age': 22}
>>> print(age)
22
>>> ###########################################################
>>> 
>>> #Python Dictionary pop() - The pop() method removes and returns an element from a dictionary having the given key.
>>> #Return value from pop() - The pop() method returns:
#If key is found - removed/popped element from the dictionary
#If key is not found - value specified as the second argument (default)
#If key is not found and default argument is not specified - KeyError exception is raised
>>> 
>>> 
>>> 
>>> #Pop an element from the dictionary:
>>> 
>>> sales = {'apple':2, 'orange':3, 'grapes':4}
>>> element=sales.pop('apple')
>>> print(element)
2
>>> print(sales)
{'orange': 3, 'grapes': 4}
>>> sales
{'orange': 3, 'grapes': 4}
>>> 
>>> 
>>> #Pop an element not present from the dictionary:
>>> sales = {'apple':2, 'orange':3, 'grapes':4}
>>> element = sales.pop('guava')
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    element = sales.pop('guava')
KeyError: 'guava'
>>> 
>>> #Pop an element not present from the dictionary, provided a default value:
>>> 
>>> sales = {'apple':2, 'orange':3, 'grapes':4}
>>> element = sales.pop('guava','banana')
>>> print(element)
banana
>>> print(sales)
{'apple': 2, 'orange': 3, 'grapes': 4}
>>> 
>>> 
>>> ##############################################################
>>> #Python Dictionary values() - The values() method returns a view object that displays a list of all the values in the dictionary.
>>> #Get all values from the dictionary:
>>> sales = {'apple':2, 'orange':3, 'grapes':4}
>>> print(sales.values())
dict_values([2, 3, 4])
>>> 
>>> 
>>> #How values() works when dictionary is modified?
>>> sales = {'apple':2, 'orange':3, 'grapes':4}
>>> print(sales)
{'apple': 2, 'orange': 3, 'grapes': 4}
>>> values = sales.values()
>>> print(values)
dict_values([2, 3, 4])
>>> 
>>> del[sales['apple']]
>>> print(sales)
{'orange': 3, 'grapes': 4}
>>> print(values)
dict_values([3, 4])
>>> 
>>> ###############################################################
>>> #Python Dictionary update() - The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.
>>> 
>>> #Working of update():
>>> d = {1:'one',2:'three'}
>>> d1 = {2:'two'}
>>> d.update(d1) #updates the value of key 2
>>> print(d)
{1: 'one', 2: 'two'}
>>> d1={3:'Three'}
>>> d.update(d1)#adds element with key 3
>>> print(d)
{1: 'one', 2: 'two', 3: 'Three'}
>>> 
>>> 
>>> #update() When Tuple is Passed:
>>> d = {'x':2}
>>> d.update(y=3,z=0)
>>> print(d)
{'x': 2, 'y': 3, 'z': 0}
>>> 
>>> 

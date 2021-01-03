def eggs(arg):
    arg.append('Hello')

spam = [1,2,3]
eggs(spam) #Here it passes a reference to list and thus spam gets appended with 'Hello'
print(spam)
#Output: [1, 2, 3, 'Hello']

spam = ['A', 'B', 'C', 'D']
cheese = spam #Here reference id to list has been copied to cheese, both cheese and spam are refering to same list in memory
cheese[1] = 42
print(cheese)
print(spam)
#Output:
#['A', 42, 'C', 'D']
#['A', 42, 'C', 'D']


#when we need a completely seperate copy of list:
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
#output:
#['A', 42, 'C', 'D']
#['A', 'B', 'C', 'D']


#Line continuation
#There is an exception for list value indentation
spam = ['apples',
        'oranges',
        'banaans',
        'cats']

print(spam)
#\ tells to ignore the indentation on next line
print('Four score and seven' + \
      ' years ago')
#output: ['apples', 'oranges', 'banaans', 'cats']
#Four score and sevenyears ago



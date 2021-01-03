spam = 42 #global variable

def eggs():
    spam = 42 #local variable
    print(spam)

print('Some code here')#global
print('Some code here')#global



#To assign a value to global variable in function scope:

def eggs2():
    global spam #if we do not inform spam is global, spam will be created in eggs2 local scope as a local variable
    spam = 50
    print(spam)

eggs()
eggs2()

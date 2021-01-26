spam = 42 #global variable

def fun1():
    spam = 40 #local variable
    print(spam)

print('Some code here')#global
print('Some code here')#global



#To assign a value to global variable in function scope:

def fun2():
    global spam #if we do not inform spam is global, spam will be created in fun2 local scope as a local variable
    spam = 50
    print(spam)

fun1()
fun2()

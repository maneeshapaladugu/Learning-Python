#To avoid the entire program crash
def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero')

print(div42by(2))  #21.0
print(div42by(12)) #3.5
print(div42by(0))  #Error: You tried to divide by zero
                   #None
print(div42by(1))  #42.0



#int('6')  -> Output: 6
#int('six') -> Output: ValueError: invalid iteral for int() with base 10: 'six'



print('How many computers do you have?')
numComp = input()
try:
    assert int(numComp) > 0  #Test if it is True
    if int(numComp) >= 4:
        print('That is a lot of computers')
    else:
        print('That is not that many computers')
except ValueError:
    print('You did not enter a number')
except AssertionError:
    print('You entered a negative number')






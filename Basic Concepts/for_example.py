#using while loop
print('My name is')
i=0
while i < 5:
    print('Printing Jimmy 5 times ' + str(i))
    i = i + 1

#****************************************************
    
#using for loop
#range(5)     #evaluates to range(0,5)  -> 0 to 4 range
#range(12,16) #evaluates to range(12,16)-> 12 to 15 range
#range(0,10,2)#evaluates to range(0,10,2) Here, 3rd arg is the step arguement -> 0 to 9 - each time incrementing by 2
    #(For example, 0,2,4,6,8)
#range(5,-1,-1)#evaluates to range(5,-1,-1) Here, 3rd arg is the step arguement -> 5 to 0 - each time decrementing by 1
    #(For example, 5,4,3,2,1,0)
    
print('My name is')
#for i < 5:  #invalid syntax error
for i in range (5): #i starts with 0 and elevates the assignment/increment operation on i
    print('Printing Jimmy 5 times ' + str(i))

    


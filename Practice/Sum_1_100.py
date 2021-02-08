#Python program to calculate sum of numbers in a given range
s = 0
count = 100

while count:
    s += count
    count -= 1
print("Sum of numbers from 1 - 100 is\n",s)

############################################################

s = 0 
print("Enter the range of numbers for addition")
n1 = int(input("Enter the minimum number"))
n2 = int(input("Enter the maximum number"))

for i in range (n1, n2+1):
    s += i

print("Sum of numbers from %d to %d is" %(n1,n2),s)

#Python program to check whether number is positive or negative
#Method 2
import sys
num = int(input("Enter a number:\n"))
size_of_num = sys.getsizeof(num)
print(size_of_num)
if num>>size_of_num & 1:
    print("%d is nagative number" %(num))
else:
    print("%d is positive number" %(num))        

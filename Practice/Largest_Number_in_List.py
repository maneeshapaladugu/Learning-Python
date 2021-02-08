#Python program to fing the largest number in a given 0

numList = []  #Empty list
n = int(input("Enter the number of elements to be in list:\n"))
print("Enter elements:")
for i in range(n):
   element = int(input())
   numList.append(element)

print("Elements in the list: ", numList)

big = 0
for i in numList:
    if i>big:
        big = i

print("Largest number in the list: ", big)

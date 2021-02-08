#Python program to find the second largest number in a list

numList = [] #Empty list to append the numbers in to it
n = int(input("Enter no of elements\n"))
print("Enter the elements")

for i in range (n):
    numList.append(int(input()))
print("Your list is ready: {}".format(numList))

numList.sort(reverse=True)
print("List in Descending order: {}".format(numList))
print("Second largest number in given list is :", numList[1])

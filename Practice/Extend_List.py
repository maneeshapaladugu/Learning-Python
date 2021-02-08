#Python program to extend a list with another list and sort it

list1 = []
list2 = []

n1 = int(input("Enter the number of elements to be in list1:"))
n2 = int(input("Enter the number of elements to be in list2:"))

print("Enter elements for list1:")
for i in range(n1):
    list1.append(input())

print("Enter elements for list2:")
for i in range(n2):
    list2.append(input())

list1.extend(list2)
print("Extended list1:", list1)

list1.sort()
print("Sorted list1: ", list1)

print("list2:", list2)

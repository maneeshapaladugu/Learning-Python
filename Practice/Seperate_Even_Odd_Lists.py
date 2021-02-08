#Python program to seperate even elements and odd elements of a list in to two different lists

def seperateLists(numList):
    evenList = []
    oddList = []

    for i in numList:
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    return (evenList,oddList)


num_List = []
n = int(input("Enter the no of elements"))
print("Enter the elements")

for i in range(n):
    num_List.append(int(input()))
print("Your list is here : {}".format(num_List))

(even_List,odd_List) = seperateLists(num_List)
print("Even List: {}".format(even_List))
print("Odd List: {}".format(odd_List))

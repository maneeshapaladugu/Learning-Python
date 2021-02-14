numList = [10, 5, 9, 20, 15]

for i in range(0, len(numList)-1):
    for j in range(0, len(numList)-i-1):
        if numList[j] > numList[j+1]:
            numList[j], numList[j+1] = numList[j+1], numList[j]
print(numList)

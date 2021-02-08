#Python program to multiply dictionary values

dict = {'A': 10, 'B':5, 'C':15}

total = 1
for key in dict:
    total *= dict[key]

print("Total: ",total)


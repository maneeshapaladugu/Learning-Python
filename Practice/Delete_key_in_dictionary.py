#Python program to remove the given key from dictionary
dict = {'a':1,'b':2,'c':3,'d':4}

print("Dictionary:")
print(dict)

key = input("Enter a key(a-d) to delete from dictionary:\n")

if key in dict:
    del dict[key]
else:
    print("Key not found in dictionary")

print("Dictionary:")
print(dict)

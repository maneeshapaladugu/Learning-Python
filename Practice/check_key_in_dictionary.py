#Python program to check whether given key exists in a dictionary or not

#Method 1
dict = {'id':10, 'name':'Joe', 'role':'Engineer', '100': 200}

key = input("Enter key:\n")
if key in dict.keys():
    print(key + " is present in dictionary and its value is: " + str(dict[key]))
else:
    print(key + " key is not present in dictionary")



#Method 2
dict = {100:200, 300:400, 500:600}

key = int(input("Enter integer key:\n"))#Received input as an integer
if key in dict.keys():
    print(str(key) + " is present in dictionary and its value is: " + str(dict[key]))
else:
    print(str(key) + " key is not present in dictionary")

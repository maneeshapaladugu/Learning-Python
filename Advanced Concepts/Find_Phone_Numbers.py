#Python program to find the phone numbers from a text

def isPhoneNumber(text):  #415-555-
    if len(text) != 12:
        return False #Not phone number sized
    for i in range(0,3):
        if not text[i].isdecimal():
            return False #No area code
    if text[3] != '-':
        return False #Missing first dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False #NO first 3 digits
    if text[7] != '-':
        return False #Missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False #Missing last 4 digits
    return True

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12] #Starting from index 0, we move one step forward and collect 12 characters
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)
        foundNumber = True
if not foundNumber:
        print('Could not find any phone numbers.')


#Output:
#Phone number found: 415-555-1011
#Phone number found: 415-555-9999


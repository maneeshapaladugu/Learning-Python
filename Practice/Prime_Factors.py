#Python program to calculate the prime factors of an integer

def isPrime(num):
    if num == 2:
        return 1

    for i in range(2,num): #Here loop starts with i=2 and ends with i=num-1
        if num % i == 0:
            return 0
    return 1

num = int(input("Enter a number:\n"))
print("The prime factors of %d are:" %(num))

for i in range(2,num//2+1): #as the loop ends with one number backward, we are adding one to it
    if num % i == 0:
        if isPrime(i):
            print(i)

#Python program to calculate the prime factors of an integer

def isPrime(num):
    if num == 2:
        return 1

    for i in range(2,num):
        if num % i == 0:
            return 0
    return 1

num = int(input("Enter a number:\n"))
print("The prime factors of %d are:\n" %(num))

for i in range(2,num//2+1):
    if num % i == 0:
        if isPrime(i):
            print(i)

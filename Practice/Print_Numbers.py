#Python program to print numbers in a range that are divisible by a given number

print("Enter the min, max ranges and the divisor")
minimum = int(input("Enter min\n"))
maximum = int(input("Enter max\n"))
divisor = int(input("Enter Divisor\n"))

print("Numbers that are divisible by " + str(divisor) + " are:")
for i in range(minimum,maximum+1):
    if i % divisor == 0:
        print("%d" %(i))

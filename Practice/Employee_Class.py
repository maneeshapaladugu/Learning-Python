#Class Variables — Declared inside the class definition (but outside any of the instance methods). They are not tied to any particular object of the class,
#hence shared across all the objects of the class. Modifying a class variable affects all objects instance at the same time.

#Instance Variable — Declared inside the constructor method of class (the __init__ method).
#They are tied to the particular object instance of the class, hence the contents of an instance variable are completely independent from one object instance to the other.


#Employee class
class Employee:
    EmployeeCount = 5 #Class variable
    def __init__(self,first,last,pay): #Constructor receives the instance as argument. self is same as this pointer in c++
        self.firstname = first #Instance variable
        self.lastname = last
        self.salary = pay

    def fullname(self):
        return "{} {}".format(self.firstname,self.lastname)

emp = Employee("Maneesha", "Paladugu", 1000)

print(emp.fullname())#from instance
print(emp.EmployeeCount)
print(Employee.fullname(emp))#from class
print(Employee.EmployeeCount)

#Output:
#Maneesha Paladugu
#5
#Maneesha Paladugu
#5

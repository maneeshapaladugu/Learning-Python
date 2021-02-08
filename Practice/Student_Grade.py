#Python program to input marks of a student in 6 subjects and display the grade

def studentGrade():
    marksList = []
   
    for i in range(1,7):
        num = int(input("Marks of Subject[%d]:"%(i)))
        marksList.append(num)
        
    total = sum(marksList)
    percentage = (total / 6)
       
    if percentage >= 75:
        print("Student grade is A")
    elif percentage >= 45 and percentage <= 75:
        print("Student grade is B")
    else:
        print("Student grade is C")

print("Enter marks in all 6 subjects")
studentGrade()

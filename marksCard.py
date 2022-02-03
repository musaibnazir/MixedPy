print('Marks Card (Marks Out of 100)')
math=float(input("Enter Math Marks: "))
science=float(input("Enter Science Marks: "))
english=float(input("Enter english Marks: "))
socialScience=float(input("Enter social science Marks: "))
urdu=float(input("Enter urdu Marks: "))

total_marks = 500
total_marks_obtained  = math + science + english + socialScience + urdu
percentage = (total_marks_obtained / total_marks)*100
print("Total Marks: "+str(total_marks))
print("Marks Obtained: "+str(total_marks_obtained))
print("Percentage: "+str(percentage)+"%")

if percentage > 75:
    print("Grade :Distinsion")
    print("Congratulations")
elif percentage > 65 and percentage < 75:
    print("Grade: A")
    print("Well Done")
elif percentage > 50 and percentage < 65:
    print("Grade: B")
    print("Work Hard")
else:
    print("Grade: Fail")
    print("You cant Make it.Better Luck Next Time. ")
    

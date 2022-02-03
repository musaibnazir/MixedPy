print("Table Generator: ")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter last Number: "))
while num1 <= num2:
    print("Table of ",num1,'is: ')
    a=1
    while a <=10:
        print(num1,"X",a,"=", num1*a)
        a=a+1
    num1=num1+1
    print()
    

print("Table Generator Range: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter last number: "))
for i in range(num1,num2+1):
    print("Table of ",i,":")
    for j in range(1,11):
        print(i,"X",j,"=",i*j)
    print()       
    

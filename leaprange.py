print("Leap Year Range Calculator: ")
num1 = int(input("Enter First Year: "))
num2 = int(input("Enter last Year: "))

for i in range(num1,num2):
    if i % 4 == 0 and i % 100 != 0:
        print(i, "is a Leap Year")
    elif i % 400 ==0:
        print(i, "is a Leap Year")
    


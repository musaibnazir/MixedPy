print("Leap Year Range Calculator: ")
year1=int(input("Enter First Year: "))
year2 = int(input("Enter Last Year: "))
while year1<=year2:
    if year1 % 4 == 0 :
        print(year1,"is a leap year")
    year1= year1 + 1    

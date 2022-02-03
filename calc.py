class calc:
    def add(self,a,b):
        c = a + b
        return str(c)

    def sub(self,a,b):
        c = a - b
        return str(c)

    def mult(self,a,b):
        c = a * b
        return str(c)

    def div(self,a,b):
        c = a / b
        return str(c)

    def welcome(self):
        print("press 1 for Addition ")
        print("press 2 for Subtraction ")
        print("press 3 for Multiplication ")
        print("press 4 for Division ")
        print("press 5 to Exit ")

print("Welcome to calculator Program")
while True:
    print()
    mc= calc()
    mc.welcome()
    a=input("enter: ")
    print()
    if a == "1":
        print("Addition")
        a= int(input("Enter First Number:  "))
        b= int(input("Enter Second Number:  "))
        print("Addition: ",mc.add(a,b))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            print("Thankyou for using this program.")
            break
    elif a == "2":
        print("Subtraction")
        a= int(input("Enter First Number:  "))
        b= int(input("Enter Second Number:  "))
        print("Subtraction: ",mc.sub(a,b))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            print("Thankyou for using this program.")

            break
    elif a == "3":
        print("Multiplication")
        a= int(input("Enter First Number:  "))
        b= int(input("Enter Second Number:  "))
        print("Multiplication: ",mc.mult(a,b))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            print("Thankyou for using this program.")

            break
    elif a == "4":
        print("Division")
        a= int(input("Enter First Number:  "))
        b= int(input("Enter Second Number:  "))
        print("Division: ",mc.div(a,b))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            print("Thankyou for using this program.")
            
            break
    elif a == "5":
        print("Thankyou for using this programm")
        break
    else:
        print("Error: Invalid Input")

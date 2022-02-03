print("Welcome to temperature convertor")
class convert:
    def celcius(self,a):
        temp = a * (9/5) + 32
        return temp
    def feh(self,a):
        temp = (a-32)*(5/9)
        return temp

    def wel(self):
        print("print 1 for C to F")
        print("print 2 for F to C")

while True:
    print()
    mc= convert()
    mc.wel()
    a=input("enter: ")
    print()
    if a == "1":
        print("C to F")
        print("Enter Value in C ")
        user = int(input("Enter C: "))
        print("This value is ",mc.celcius(user))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            break
    elif a == "2":
        print("F to C")
        a= int(input("Enter F:  "))
        print("Subtraction: ",mc.feh(a))
        print()
        print("Press Y to continue.Press any Key to Exit. ")
        txt = input()
        if txt !='y':
            break

    else:
        print("Error: Invalid Input")        


print("Enter Value in C ")
user = int(input("Enter: "))
mc = convert()
print("Converting C into F ")
print("Temp: ",mc.celcius(user))

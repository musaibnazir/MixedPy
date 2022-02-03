def fib():
    a=1
    b=1
    print(a)
    for i in range(101):
        c=a+b
        print(c)
        a=b
        b=c

def leap():
    year= int(input("Enter Year you want To Find: "))
    if year % 4 == 0 and year % 100 != 0:
        print(year, "is a Leap Year")
    elif year % 100 == 0:
        print(year, "is not a Leap Year")
    elif year % 400 ==0:
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")
    
def search():
    list= [1,3,56,7,87,3,23,2]
    print(list)
    user = int(input("Enter Num to check:"))
    isfound = False
    for i in range (0,len(list)):
        if user == list[i]:
            print("No is in list at: ",i,"index")
            isfound = True

    if not isfound:
        print("Not Found!")
 

print("The fibonnacci Series is: ")
fib()
print()

print("Find The Leap Year:  ")
leap()
print()

print("Search Program")
search()
print()

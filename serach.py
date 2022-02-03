list= [1,3,56,7,87,3,23,2]

user = int(input("Enter Num to check:"))
isfound = False
for i in range (0,len(list)):
    if user == list[i]:
        print("No is in list at: ",i,"Position")
        isfound = True

if not isfound:
    print("Not Found!")
        

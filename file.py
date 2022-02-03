print("This is the File Creation Program!!")
print("Dou you want to create a file? (y/n)")
answer = input()
if answer == 'y':
    print("Type the name of the file")
    name = input()
    print("type thee extension of the file")
    ext = input()
    obj = open(name+"."+ext,"w")
    print("File Successfully created.")
    print("Do you want to write to your file?(y/n)")
    answer1= input()
    if answer1 == 'y':
        print("Enter your text her>> " )
        text = input()
        obj.write(text)
        obj.close()
        print("Text added ..Do You want to see? (y/n)")
        answer2 = input()
        if answer2 == 'y':
                obj1 = open(name+"."+ext,"r")
                str = obj1.read()
                obj1.close()
                print(str)
                print("Dou you want to write more..(y/n)")
                answer3 = input()
                if answer3 == 'y':
                    obj2 = open(name+"."+ext,"a")
                    input = input("Write Here")
                    obj2.write(input)
                    print("File Appended")
                    obj2.close()
                    obj2 = open(name+"."+ext,"r")
                    a = obj2.read()
                    print(a)
                else:
                    print("Thankyou for Using the program")



        else:
            print("Your file Has been created.. Thanku for using")

    else:
        print("Your file Has been created.. Thanku for using")
elif answer == 'n':
    print("Thanku for using our program")

else:
    print("Invalid Option.Terminated")

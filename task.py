def enter():
    while True:
        fo = open("student.xls","a")
        print("Enter the Students Detail")
        print("Enter Student S.no")
        fo.write(input() + "\t")
        print("Enter Student Name")
        fo.write(input() + "\t")
        print("Enter Student Class")
        fo.write(input() + "\t")
        print("Enter Student Marks")
        fo.write(input() + "\n")
        fo.close()
        print("Press Y to enter more values: ")
        txt = input()
        if txt !='y':
            break
    print("Enter the Students Detail")

def view():
    print("This is the Preview of the Student Detail")
    fo = open("student.xls","r")
    result = fo.read()
    fo.close()
    print(result)

def log():
    print("Press 1 for Edit")
    print("Press 2 for View")
    print("Press 3 for Exit")


while True:
    print("Welcome to student Details Program:")
    log()
    int = input()
    if int == '1':
        enter()
    elif int == '2':
        view()
    elif int =='3':
        print("Thankyou For using this Program")
        break
    else:
        print("Error: Wrong Option.. ")
        break

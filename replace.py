list = [1,23,4,5,54,23,16]
print(list)
num1 = int(input("Enter old value: "))
num2 = int(input("Enter new value: "))

flag = False

for i in range(len(list)):
    if num1 == list[i]:
        list[i]= num2
        print(list)
        flag=True;
if not flag:
    print("Number Not Found")
     

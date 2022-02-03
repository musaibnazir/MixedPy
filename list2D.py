lst = [[1,2,3],[4,5,6],[7,8,9]]
lst1 = [[100,200,300],[400,500,600],[700,800,900]]

def list(num):
    for i in range(3):
        for j in range(3):
            print(num[i][j],"",end="")
        print()

def list1(num1,num2):
    for i in range(3):
        for j in range(3):
            print((num1[i][j])-(num2[i][j]),"",end="")
        print()

print("List1 Is: ")
list(lst)
print()
print("List2 is: ")
list(lst1)
print()
print("Subtraction List1 from List2\n.......\n.... ")
print("Subtracted list is: ")
list1(lst1,lst)

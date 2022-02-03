list1 = []
list2 = []
list3 = []

def func(name):
    n = int(input("Enter Number of elements: "))

    for i in range(n):
        ele = int(input())
        name = name + [ele]
    print(name)

print("List 1: ")
print(list1)
func(list1)
print("List 2")
func(list2)
print("List 3")
func(list3)
print("Creating 2D list:")
lst = [[list1],[list2],[list3]]

for j in range(3):
    for k in range(3):
        print(lst[j][k])

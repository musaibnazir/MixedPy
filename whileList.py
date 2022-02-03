lst =[]
n= int(input("Enter No of Elements you want to add:  "))

i=0
print("Enter Elements you want to add.(one element at one time): ")
while i<=n-1:
    ele = int(input())
    lst.append(ele)
    i+=1
print("The Created List is: ",lst)
print("Sorting now")

for k in range(0,6):
    
    for l in range(0,6-k):
        print(".",end=" ")
    print()        

for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j] > lst[j+1] :
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("The Sorted List is: ",lst)


for i in range(len(lst)):
    for j in range(0,len(lst)-i-1):
        if lst[j] < lst[j-1] :
            lst[j], lst[j-1] = lst[j-1], lst[j]

print("The Sorted List is: ",lst)
                

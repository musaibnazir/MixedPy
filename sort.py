list=[1,11,12,3,5,7,2,4,6,0,10]
print(list)

for i in range(len(list)):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j+1] :
            list[j], list[j+1] = list[j+1], list[j]
print(list)
                

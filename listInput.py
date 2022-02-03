lst = []

while True:
    print('Enter Value: ')
    lst = lst + [input()]
    

    choice = input()
    if choice != 'y':
        break

print (lst)
for i in lst:
    print(i)

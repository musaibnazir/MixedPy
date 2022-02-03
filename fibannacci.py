#Fibannacci Series
print("Fibannacci Series:")
a = 1
b = 1
print(a)
for i in range(101):
    c = a + b
    print (c)
    a = b
    b = c

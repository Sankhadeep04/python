l = input("enter the elements : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
print("after reversing the list is :")
l.reverse()
print(l)
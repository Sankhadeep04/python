l = input("enter the elements : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
l1 = input("enter the elements of second list : ").split(',')
for i in range(len(l1)):
    l1[i] = int(l1[i])
l.extend(l1)
print("after marging the list is : ")
print(l)
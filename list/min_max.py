l = input("Enter the elements of the array : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
max = l[0]
min = l[0]
for _ in range (len(l)):
    if(l[_]>max):
        max = l[_]
    elif (l[_]<min):
        min = l[_]
print(f"maximum element in the list is {max}")
print(f"minimum element in the list is {min}")

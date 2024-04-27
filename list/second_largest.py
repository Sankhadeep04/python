l = input("Enter the elements of the array : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
max = l[0]
sec = l[0]
for _ in range (len(l)):
    if(l[_]>max):
        max = l[_]
for _ in range (len(l)):
    if(l[_]>sec and l[_]<max):
        sec = l[_]
print(f"the second maximum element is {sec}")
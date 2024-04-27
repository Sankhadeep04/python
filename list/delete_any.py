l = input("enter the elements : ").split(',')
n = int(input("enter the element position : "))
count = 0
for i in range(len(l)):
    l[i] = int(l[i])
if(n < 0 or n > len(l)):
    print("invalid position")
else:
    l.pop(n-1)
print(f"after deleting the list is {l}")
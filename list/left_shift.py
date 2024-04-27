l = input("enter the elements : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
n = int(input("Enter the number of times to left-rotate : "))
n = n % len(l)
print (n)
print(f"before rotation : {l}")
for j in range(n):
    temp = l[0]
    for i in range(len(l)-1):
        l[i] = l[i+1]
    l[(len(l)-1)] = temp
print("after rotating the list is :")
print(l)

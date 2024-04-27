m = int(input("Enter the number of elements : "))

l = input("enter the elements : ").split(',')
for i in range(len(l)):
    l[i] = int(l[i])
n = int(input("Enter the number of times to right-rotate : "))
n = n % len(l)
print (n)
print(f"before rotation : {l}")
for j in range(n):
    temp = l[m-1]
    i = (m-1)
    while(i > 0):
        l[i] = l[i-1]
        i+=1
    l[0] = temp
print("after rotating the list is :")
print(l)

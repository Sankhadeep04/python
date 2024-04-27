l = input("enter the elements : ").split(',')
l1 = []
n = int(input("enter the element to search : "))
for i in range(len(l)):
    l[i] = int(l[i])
temp = l.index(n)
print(f"{n} founded at {temp+1}")

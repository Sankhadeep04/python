l = input("enter the elements : ").split(',')
l1 = []

for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
print(f"after sorting the list is :{l}")
l.sort(reverse=True)
print(f"after sorting in descending order the list is :{l}")

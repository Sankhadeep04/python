l = input("enter the elements : ").split(',')
even= []
odd = []
for i in range(len(l)):
    l[i] = int(l[i])
l.sort()
for i in range(len(l)):
    if(l[i] % 2 == 0):
        even.append(l[i])
    else:
        odd.append(l[i])
# even.sort()
print(f"even list is : {even}")
print(f"odd list is :{odd}")
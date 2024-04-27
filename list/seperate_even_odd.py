l = input("enter the elements : ").split(',')
even= []
odd = []
for i in range(len(l)):
    l[i] = int(l[i])
for i in range(len(l)):
    if(l[i] % 2 == 0):
        even.append(l[i])
    else:
        odd.append(l[i])
print(f"even list is : {even}")
print(f"odd list is :{odd}")
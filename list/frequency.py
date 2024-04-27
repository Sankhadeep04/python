l = input("enter the elements : ").split(',')
l1 = []
for i in range(len(l)):
    l[i] = int(l[i])
    l1.append(-1)

for i in range(len(l)):
    count = 1
    j = i+1
    while(j < (len(l))):
        if(l[i] == l[j]):
            count += 1
            l1[j] = 0
        j+=1
    if(l1[i] != 0):
        l1[i] = count
print("frequency : ")
for k in range(len(l)):
    if(l1[k] != 0):
            print(f"{l[k]} founded {l1[k]} times")
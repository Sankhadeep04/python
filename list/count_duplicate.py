l = input("enter the elements : ").split(',')
l1 = []
count = 0
for i in range(len(l)):
    l[i] = int(l[i])
    l1.append(-1)

for i in range(len(l)):
    j = i+1
    while(j < (len(l))):
        if(l[i] == l[j]):
            count += 1
            break
        j+=1
print(f"total number of duplicate elements in the list = {count}")

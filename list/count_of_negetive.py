l = input("enter the elements : ").split(',')
count = 0
for i in range(len(l)):
    l[i] = int(l[i])
    if(l[i] < 0):
        count+=1
print(f"number of negative elements in the list is {count}")
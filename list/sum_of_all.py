l = input("Enter the elements of the array : ").split(',')
sum = 0

for i in range(len(l)):
    l[i] = int(l[i])
    sum+=l[i]
print(sum)
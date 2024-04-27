l = input("Enter the elements of the array : ").split(',')

for i in range(len(l)):
    l[i] = int(l[i])

for _ in range(len(l)):
    if (l[_] < 0):
        print (l[_])
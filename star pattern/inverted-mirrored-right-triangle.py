n = int(input("Enter number : "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end='')
    k = i
    while(k<n+1):
        print("*",end='')
        k+=1
    print()
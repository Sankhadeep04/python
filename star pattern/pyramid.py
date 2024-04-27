n = int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    k = 1
    while(k <= 2*i-1):
        print("*",end='')
        k+=1
    print()
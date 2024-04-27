n = int(input("enter the number : "))
for i in range(1,n):
    j = 1
    while(j <= (n-i)):
        print(" ",end='')
        j+=1
    for j in range(i,n+1):
        print("*",end='')
    print()
for i in range(1,n+1):
    j = 1
    while(j < i):
        print(" ",end='')
        j+=1
    for j in range(1,1+i):
        print("*",end='')
    print()

    
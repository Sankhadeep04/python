n = int(input("enter the number : "))
for i in range(1,n+1):
    for j in range(i,n):
        print(" ",end='')
    j = 1
    while(j <= (2*i-1)):
        if(j == 1 or i == n or  j == (2*i-1)):
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print()
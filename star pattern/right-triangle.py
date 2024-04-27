n = int(input("Enter number : "))
for i in range(1,n+1):
    j = i
    while(j<n):
        print(" ",end='')
        j+=1
    j = 1
    while(j<=i):
        print("*",end='')
        j+=1
    print()
n = int(input("enter the number : "))
for i in range(1,(n*2)):
    if(i == n):
        for j in range(1,n*2):
            print("*",end='')
    else:
        for j in range(1,n):
            print(" ",end='')
        print("*",end='')
    print()
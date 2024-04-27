n = int(input("Enter number : "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end='')
    j = 1
    while(j <= (n*2 - (2*i-1))):
        if(i==1 or j == 1 or j == (n*2 - (2*i-1))):
            print("*",end='')
        else:
            print(" ",end='')
        j+=1
    print()
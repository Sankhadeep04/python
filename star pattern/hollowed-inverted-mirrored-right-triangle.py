n = int(input("Enter number : "))
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end='')
    j = i
    while(j<n+1):
        if(j == i or j == n+1 or i == 1):
            print("*",end='')
        else:
            print(" ",end='') 
        j+=1
    print()
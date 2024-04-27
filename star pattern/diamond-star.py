n = int(input("enter the number : "))
temp = 1
s = n-1
for i in range(1,n*2):
    for j in range(1,s+1):
        print(" ",end='')
    for j in range(1,temp*2):
        print("*",end='')
    print()
    if(i<n):
        temp+=1
        s-=1
    else:
        temp-=1
        s+=1
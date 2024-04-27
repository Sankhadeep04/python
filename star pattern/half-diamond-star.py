n = int(input("enter the number : "))
temp = 1

for i in range(1,n*2):
    for j in range(1,temp+1):
        print("*",end='')
    if(i<n):
        temp+=1
    else:
        temp-=1
    print()
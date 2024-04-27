n = int(input("enter the number : "))
temp = n*2-1
for i in range(1,temp+1):
    for j in range(1,temp+1):
        if(i == j or (j == temp+1-i)):
            print("*",end='')
        else:
            print(" ",end='')
    print()
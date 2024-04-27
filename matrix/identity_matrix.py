r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
flag = 1
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if(i == j and mat[i][j] != 1 ):
            flag = 0
        elif(i != j and mat[i][j] != 0):
            flag = 0
for i in mat:
    print(*i,sep=" ")
if(flag == 1):
    print("The given matrix is an Identity matrix")
else:
    print("The given matrix is not an Identity matrix")

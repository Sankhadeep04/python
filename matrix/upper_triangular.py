r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
flag = 0
for i in range(r):
    for j in range(c):
        if(j < i and mat[i][j] != 0):
            flag += 1
for i in mat:
    print(*i,sep=" ")
if(flag == 0):
    print("The matrix is upper triangulr Matrix!!")
else:
    print("The matrix is not upper triangular Matrix")
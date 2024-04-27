r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if(i != j and j > i):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
for i in mat:
    print(*i,sep=" ")
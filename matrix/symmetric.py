r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
flag = 0
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
mat1 = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if(mat[i][j] != mat[j][i]):
            flag = 1
            break
for i in mat:
    print(*i,sep=" ")
if(flag ==  0):
    print("The matrix is symmetric !")
else:
    print("The matrix is not symmetric !!")

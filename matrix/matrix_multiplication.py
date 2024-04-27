r = int(input("Enter the number of rows : "))
c = int(input("enter the number of columns : "))
print("enter elements of first matrix")
mat = [[int(input("enter the elements :"))for j in range(c)]for i in range(r)]
print("enter the second matrix ")
mat1 = [[int(input("enter elements : "))for j in range(c)]for i in range(r)]
mat2 = [[0 for j in range(c)]for i  in range(r)]
for i in range(len(mat)):
    for j in range(len(mat1)):
        sum = 0
        for k in range(len(mat2)):
            mat2[i][j] += mat[i][k] * mat1[k][j]
print("first matrix is ")
for i in mat:
    print(*i,sep="  ")
print("second matrix is ")
for i in mat1:
    print(*i,sep="  ")
print()
print("result")
for i in mat2:
    print(*i,sep="  ")
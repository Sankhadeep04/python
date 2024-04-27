r = (int(input("enter the number of rows : ")))
c = (int(input("enter the number of columns : ")))
print("enter elements for first matrix")
mat = [[int(input("enter the elements :"))for j in range(c)]for i in range(r)]
print("enter elements for second matrix")
mat2 = [[int(input("enter elements :"))for j in range(c)]for i in range(r)]
mat3 = [[0 for j in range(c)]for i in range(r)]
for i in range(r):
    for j in range(c):
        mat3[i][j] = mat[i][j] - mat2[i][j]
print("result")
for i in mat3:
    print(*i,sep=" ")
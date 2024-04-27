r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
sum = 0
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
print("enter elements for second list ")
mat2 = [[int(input("enter the elemets :"))for j in range(c)] for i in range(r)]
print("First matrix =>")
for i in mat:
    print(*i,sep=",")
print("Second matrix =>")
for i in mat2:
    print(*i,sep=",")
for i in range(r):
    for j in range(c):
        if (mat[i][j] != mat2[i][j]):
            flag = 1
            break
if (flag == 1):
    print("Both matrices are not equal")
else:
    print("both matrices are equal!!")
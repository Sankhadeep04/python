r = int(input("Enter the number of rows : "))
c = int(input("enter the number of columns : "))
print("enter elements of first matrix")
mat = [[int(input("enter the elements :"))for j in range(c)]for i in range(r)]
for i in range(r):
    sum = 0
    for j in range(c):
        sum += mat[i][j]
    print(f"sum of row {i+1} : {sum}")
for i in range(r):
    sum = 0
    for j in range(c):
        sum += mat[j][i]
    print(f"sum of column {i+1} : {sum}")
 
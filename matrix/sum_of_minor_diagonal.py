r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
sum = 0
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
n = len(mat)
for i in range(r):
    sum += mat[i][n-i-1]
print(f"sum of minor diagonal of the matrix is {sum}")
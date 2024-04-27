r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
sum = 0
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
for i in range(r):
    sum += mat[i][i]
print(f"sum of main diagonal of the matrix is {sum}")
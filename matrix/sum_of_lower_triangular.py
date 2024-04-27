r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
sum = 0
for i in range(r):
    for j in range(c):
        if(j < i):
            sum += mat[i][j]
print("the matrix ->")
for i in mat:
    print(*i,sep=" ")
print(f"the sum of upper triangular matrix is {sum}")  
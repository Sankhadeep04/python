r = int(input("enter the number of rows : "))
c = int(input("enter the number of columns : "))
sum = 0
print("enter elements in first list")
mat = [[int(input("enter the elements : "))for j in range(c)] for i in range(r)]
for i in range(r):
    for j in range(c):
        if(mat[i][j] == 0):
            sum+=1
if(sum >= (i * j)/2):
    print("The given matrix is sparse matrix !!")
else:
    print("The given matrix is not a sparse matrix ")
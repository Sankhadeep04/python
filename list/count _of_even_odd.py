l = input("Enter the elements of the array : ").split(',')
even = 0
odd = 0
for i in range(len(l)):
    l[i] = int(l[i])
    if(l[i] % 2 == 0):
        even+=1
    else:
        odd+=1
print(f"number of even elements in the list is {even} and number of odd elements is {odd}")

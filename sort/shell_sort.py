def sort(list):
    n = len(list)
    gap = n//2

    while(gap > 0):
        for i in range(gap,n):
            temp = list[i]
            j = i
            while(j >= gap and list[j - gap] > temp):
                list[j] = list[j - gap]
                j-=gap
            list[j] = temp
        gap //= 2       

my_list = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)

print(my_list)
print ("After sorting the list is : ")
sort(my_list)
print(my_list)
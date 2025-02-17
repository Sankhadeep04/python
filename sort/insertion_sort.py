def sort(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while (j > 0 and arr[j - 1] > arr[j]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1

    return arr


n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
print("before sorting the list is ")
print(my_list)
print("After sorting the list is ")
sort_2 = sort(my_list)
print(sort_2)
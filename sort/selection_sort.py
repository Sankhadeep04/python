def sort(list):
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if list[j] < list[min]:
                min = j
        min_value = list.pop(min)
        list.insert(i, min_value)
    return list


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
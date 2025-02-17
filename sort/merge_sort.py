def sort(list,low,high):
    if(low == high):
        return
    mid = (low + high) // 2
    sort (list,low,mid)
    sort (list,mid+1,high)
    merge(list,low,mid,high)
    
def merge(list,low,mid,high):
    temp = []
    left = low
    right = mid + 1

    while(left <= mid and right <= high):
        if(list[left] < list[right]):
            temp.append(list[left])
            left += 1
        else:
            temp.append(list[right])
            right += 1

    while(left <= mid):
        temp.append(list[left])
        left += 1
    while(right <= high):
        temp.append(list[right])
        right += 1
    for i in range(low, high + 1):  
        list[i] = temp[i - low]

    return list
        

n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
print("before sorting the list is ")
print(my_list)
print("After sorting the list is ")
sort_2 = sort(my_list,0,n-1)
print(my_list)
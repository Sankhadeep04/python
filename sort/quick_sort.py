def sort(list,low,high):
    if(low < high):
        partition = pivot(list,low,high)
        sort(list,low,partition - 1)
        sort(list,partition+1,high)


def pivot(list,low,high):
    piv = list[low]
    i = low
    j = high
    while(i < j):
        while(list[i] <= piv and i < high):
            
            i+=1
        while(list[j] > piv and j > low):

            j-=1
        if(i < j):
            list[i],list[j] = list[j],list[i]

    list[low],list[j] = list[j],list[low]   
    return j




n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
print("before sorting the list is ")
print(my_list)
print("After sorting the list is ")
sort(my_list,0,n-1)
print(my_list)
def binarySearch( arr, l, r, x):
    if r >= l:
        mid = l + ( r-l ) // 2
         
        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
         
    return -1

def exponential_search(list,n):

    i = 1
    max = len(list)
    if list[0] == n:
        return 0
    else:
        while( i < max and list[i] <= n):
           i*=2

        return binarySearch(list,i // 2,min(i,max-1),n)



list = [1,2,3,5,6,7,9,10,15,16]
n = int(input("Enter the number : "))

pos = exponential_search(list,n)

if pos == -1:
    print("Not found in the list")
else:
    print("Element found at ",pos)

def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1

        pos = low + ((x - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = int(input("Enter element to search :"))
xyz = 10
index = interpolation_search(arr, x)
print(f"Element found at index: {index}" if index != -1 else "Element not found")

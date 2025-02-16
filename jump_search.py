import math

def jump_search(arr, x, n):
    step = int(math.sqrt(n))  # Step size
    prev = 0

    # Finding the block where the element might be present
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:  # Element not found
            return -1

    # Linear search within the identified block
    for pos in range(prev, min(step, n)):
        if arr[pos] == x:
            return pos

    return -1  # Element not found

# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = int(input("Enter element to search: "))
n = len(arr)

index = jump_search(arr, x, n)
print(f"Element found at index: {index + 1}" if index != -1 else "Element not found")

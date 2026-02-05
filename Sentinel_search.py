def sentinel_search(arr, key):
    n = len(arr)
    
    # Save the last element
    last = arr[n - 1]
    
    # Place the key as a sentinel
    arr[n - 1] = key
    
    i = 0
    while arr[i] != key:
        i += 1
    
    # Restore the last element
    arr[n - 1] = last
    
    # Check if key was found
    if i < n - 1 or last == key:
        return i
    else:
        return -1


# Example usage
arr = [10, 20, 30, 40, 50]
key = 40

result = sentinel_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

# Reverse Array
def reverse_array(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr


# Second Largest Element
def second_largest(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second


# Maximum Subarray Sum (Kadane)
def max_subarray(arr):
    max_sum = current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


# Main
arr = [2, -3, 4, -1, 2, 1]

print("Original:", arr)
print("Reversed:", reverse_array(arr.copy()))
print("Second Largest:", second_largest(arr))
print("Max Subarray Sum:", max_subarray(arr))

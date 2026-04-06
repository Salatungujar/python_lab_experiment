def split_and_add(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    # split the array into two parts
    first_part = arr[:k]
    second_part = arr[k:]
    # add first and second parts
    return second_part + first_part

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = split_and_add(arr, k)
print("The original array is:", arr)
print("The result of splitting and adding the array is:", result)

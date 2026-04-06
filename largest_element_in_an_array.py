def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]

    for element in arr:
        if element > largest_element:
            largest_element = element

    return largest_element

# Example usage
my_array = [3, 4, 5, 1, 7, 8, 5]
result = find_largest_element(my_array)
print("The largest element in the array is:", result)

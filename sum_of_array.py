#Finding sum of array using sum()
arr = [1,2,3,4,5]
total = sum(arr)
print("Sum of the array is : ", total)

#function to find sum of array using recursion
def sum_of_array(array):
    total = 0 #Initialize a variable to store the sum
    
    for element in array:
        total += element #Add each element to the total
    return total

#Example usage
array = [4,5,6,7,8,9]
result = sum_of_array(array)
print("The sum of the array is : ", result)
        

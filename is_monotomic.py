def is_monotomic(arr):
    increasing = decreasing = True
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            increasing = False
        elif arr[i] < arr[i-1]:
            decreasing = False
    
    return increasing or decreasing

#Test the function
arr1 = [1,2,2,3] # Monotomic increasing
arr2 = [3,2,1]  #Monotomic decreasing
arr3 = [1,3,4,1] #Not Monotomic

print("Arr1 is monotomic : ", is_monotomic(arr1))
print("Arr2 is monotomic : ", is_monotomic(arr2))
print("Arr3 is monotomic : ", is_monotomic(arr3))

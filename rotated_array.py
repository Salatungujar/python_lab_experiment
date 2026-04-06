def rotate_array(arr,d):
    num = len(arr)
    
    if d < 0 or d >= num:
        return "Invalid number of rotations"
    
    rotated_array = [0]*num
    
    for i in range(num):
        rotated_array[i] = arr[(i + d) % num]
    return rotated_array 
    
arr = [1,2,3,4,5,6,7]
d = 3
result = rotate_array(arr,d)
print("The rotated array is : ", result)

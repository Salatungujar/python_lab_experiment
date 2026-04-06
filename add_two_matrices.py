#function to add two matrices
def add_matrices(mat1, mat2):
    #check if the matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions"

    #initialize the result matrix with zero
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

#example usage
mat1 = [
    [6,7,8],
    [7,2,1],
    [8,4,0]
]
mat2 = [
    [1,2,3],
    [7,3,5],
    [12,0,3]
]
#calling the function to add the two matrices
result_matrices = add_matrices(mat1,mat2)
#Display the result
if isinstance(result_matrices , str):
    print(result_matrices)
else:
    print("The sum of the two matrices is : ")
    for row in result_matrices:
        print(row)

#Calculate the cube of the sum of first n natural numbers
def cube_sum_of_natural_numbers(num):
    if num <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1,num+1)])
        return total
num = int(input("Enter a number : "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    result = cube_sum_of_natural_numbers(num)
    print(f"The cube of the sum of first {num} natural numbers is: {result}")

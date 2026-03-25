#Input two variables
a = input("Enter the value of the first variable (a) : ")
b = input("Enter the value of the second variable (b) : ")

#Display the original values
print(f"Original values : a = {a}, b = {b}")

#swap the values using a temprory variable
temp = a
a = b
b = a
b = temp

#Display the swapped values
print(f"Swapped values : a = {a}, b ={b}")

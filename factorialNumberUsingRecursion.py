#factorial of a number using recursion
def recur_factoiral(n):
    if n == 1:
        return n
    else:
        return n * recur_factoiral(n-1)
num = int(input("Enter a number : "))

#Check if the number is negative
if num < 0:
    print("Sorry, Factorial doesnot exist for negative numbers")
elif num == 0:
    print("The factoial of ) is 1")
else:
    print("The factorial of ", num , "is : " , recur_factoiral(num))

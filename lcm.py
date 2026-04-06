#python program to find lcm of two numbers

from numpy import greater, lcm
def compute_lcm(x,y):
    if x > y:   #Choose greater number
        greater = x
    else:
        greater = y
    while(True):
        if((greater%x ==0) and (greater%y == 0)):
            lcm = greater 
            break
        greater += 1

    return lcm

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number :"))

print("The LCM is ", compute_lcm(num1,num2))

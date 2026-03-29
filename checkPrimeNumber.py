num = int(input("Enter a number : "))

#define a flag variable
flag = False
if num == 0:
    print("{0} is not a prime number")
elif num > 1:
    #checks for factors
    for i in range (2,num):
        if(num%2 == 0):
            flag = True #if factor is found, set flag is True
            #break out of loop 
            break
    #check if falg is True
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number ")    

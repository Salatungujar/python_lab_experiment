lower = int(input("Enter Lower Limit :"))
upper = int(input("Enter upper Limit :"))

for num in range (lower,upper+1): #Iterative through the numbers
    order = len(str(num)) #calcuate the number of digits in the number
    
    temp_num = num
    sum = 0
    
    while temp_num > 0:
        digit = temp_num % 10
        sum  += digit ** order
        temp_num //= 10
        
if num == sum :
    print(num)      

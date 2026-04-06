limit = int(input("Enter the limit : "))

#initialize the sum
sum = 0

#use for loop to iterate through the natural numbers and add them to sum
for i in range(1,limit+1):
    sum += i
    
    #print the sum
print("The sum of nutural number upto" , limit , " is :", sum)
     

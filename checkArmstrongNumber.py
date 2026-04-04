num = int(input("Enter a number :"))

#caculate the number of digits in the numbr
num_str = str(num)
new_digits = len(num_str)

#Intialize sum
sum_of_powers = 0
temp_num = num

#calculate the sum of the digits raised to the power of the number of digits
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** new_digits
    temp_num //= 10

#check if it's an Armstrong number

if sum_of_powers == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number ")    

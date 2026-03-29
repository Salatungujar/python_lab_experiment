year = int(input("Enter a year : "))

#divided by 100 means by 400 is leap year (ending with 00 )
#century year divided by 400 is leap year

if(year%400 == 0) & (year%100 == 0):
    print("{0} is a leap year " .format(year))
    
#not divided by 100 means not a century year
#year divided by 4 is leap year

elif(year%4 == 0) & (year%100 != 0):
    print("{0} ) is a leap year " .format(year))
    
#if not divided by 400 (century year) & 4 (not century year)
#year is not leap year    
else:
    print("{0} is not a leap year " .format(year))  

kilometers = float(input("Enter distance in kilometers :"))

#conversion factor : 1 kilometers = 0.621371 times
conversion_factor  = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

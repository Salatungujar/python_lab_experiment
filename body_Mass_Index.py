def bodymassindex(height,weight):
    return round((weight/height**2),2)

height = float(input("Enter your height in meters :"))
weight = float(input("Enter your weight in kg :"))

print("Welcome to the BMI calculator !")

bmi = bodymassindex(height,weight)
print("Your BMI is : ", bmi )

if bmi <= 18.5:
    print("Your weight is underweight" )
elif 18.5 < bmi <= 24.5:
    print("Your weight is normal")
elif 24.5 < bmi <= 29.9:
    print("Your weight is overweight")
else:
    print("Your weight is obese")

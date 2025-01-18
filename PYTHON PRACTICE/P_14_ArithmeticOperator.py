#BMI Calculator
weight=float(input("Enter Your weight in kg: "))
height=float(input("Enter your height in cm: "))
height_m=height/100
Calculate_BMI=weight/(height_m**2)
print("Your Body-Mass-Index is: %.2f" %Calculate_BMI)
name = input('What is your name : ')
weight = float(input('Enter your weight as Kg : '))
height = float(input('Enter your height as meters : '))

# BMI = kg/m2
# below 18.5 – you're in the underweight range
# between 18.5 and 24.9 – you're in the healthy weight range
# between 25 and 29.9 – you're in the overweight range
# between 30 and 39.9 – you're in the obese range

calc_BMI = weight / (height**2)
if ()
print("BMI : ", round((calc_BMI), 2))

name = input('What is your name : ')
weight = float(input('Enter your weight as Kg : '))
height = float(input('Enter your height as meters : '))

# BMI = kg/m2
calc_BMI = weight / (height**2)
print("BMI : ", round(calc_BMI)

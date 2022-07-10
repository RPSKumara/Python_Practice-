name = input('What is your name : ')
weight = intinput('Enter your weight as Kg : ')
height = int(input('Enter your height as meters : '))

# BMI = kg/m2
calc_BMI = weight / (height**2)
print("BMI : ", calc_BMI)

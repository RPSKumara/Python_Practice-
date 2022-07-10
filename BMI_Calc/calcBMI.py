name = input('What is your name : ')
weight = float(input('Enter your weight as Kg : '))
height = float(input('Enter your height as meters : '))

# BMI = kg/m2
# below 18.5 – you're in the underweight range
# between 18.5 and 24.9 – you're in the healthy weight range
# between 25 and 29.9 – you're in the overweight range
# between 30 and 39.9 – you're in the obese range

calc_BMI = round((weight / (height**2)), 2)
if (calc_BMI > 0 and calc_BMI < 39.9):
    if (calc_BMI < 18.5):
        print(name, "pay attention your in underweight range your BMI : ",
              calc_BMI)
    elif (calc_BMI > 18.5 and calc_BMI < 25):
        print(name, "congratulation you're in the healthy weight range your BMI : ",
              calc_BMI)
    elif (calc_BMI > 25 and calc_BMI < 30):
        print(name, "pay attention you're in the overweight range your BMI : ",
              calc_BMI)
    else:
        print(name, "pay attention you're in the obese range your BMI : ",
              calc_BMI)
else:
    print(name, " Please enter correct Information")

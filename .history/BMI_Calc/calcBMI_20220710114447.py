name = input('What is your name : ')


try:
    weight = float(input('Enter your weight as Kg : '))
    height = float(input('Enter your height as meters : '))



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


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

height=float(input('\nPlease enter you height in centimetres: '))
weight=float(input('\nPlease enter your weight in kilograms: '))
BMI=weight/(height/100)**2
if BMI<18.5:
    print('You are underweight.')
elif BMI<=24.9:
    print('You are healthy. :)')
elif BMI <=29.9:
    print('You are overweight.')
elif BMI<=34.9:
    print('You are obese')
else:
    print('You are extremely obese.')
height = float(input('Please Enter your height in metres: '))
weight = float(input('Please Enter your weight in kg: '))

bmi = weight/(height ** 2)

print(round(bmi,2))

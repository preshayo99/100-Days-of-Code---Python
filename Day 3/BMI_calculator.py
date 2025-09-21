height = float(input('Please Enter your height in metres: '))
weight = float(input('Please Enter your weight in kg: '))

bmi = weight/(height ** 2)

print(round(bmi,2))

if bmi >= 25:
    print("overweight")
elif bmi >= 18.5:
    print("normal weight")
else:
    print("underweight")
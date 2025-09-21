BOLD = '\033[1m'
RESET = '\033[0m'


print(F'{BOLD}Welcome to the tip calculator!{RESET}')

Total_bill = float(input('What was the total bill? £'))
Tip = int(input('How much would you like to tip? 10%, 12% or 15%? '))
people_split = int(input('How many people would you like to split the bill with? '))

Final_bill =(Total_bill*(1+Tip/100))/people_split


print(f'Each person should pay: £{Final_bill:.2f}')


''' print('Welcome to the rollercoaster!')
height = int(input('What is your height in cm?: '))
age = int(input('How old are you?: '))

if  height >= 120:
    print('You can ride the rollercoaster!')
    if age <= 12:
        print('That will cost £5.00')
    elif age > 12 and age < 18:
        print('That will cost £7.00')
    else:
        print('That will cost £10.00')
else:
    print('Sorry, you have to grow taller before you can ride.')print('Welcome to the rollercoaster!')
'''

print('\nWelcome to the rollercoaster!\n')
height = int(input('What is your height in cm?: '))
age = int(input('How old are you?: '))
bill = 0

if  height >= 120:
    print('\nYou can ride the rollercoaster!\n')
    if age <= 12:
        bill = 5
        print('That will cost £5.00')
    elif age > 12 and age < 18:
        bill = 7
        print('That will cost £7.00')
    else:
        bill = 10
        print('That will cost £10.00')
        
    picture = (input('Would you like a picture yes or no?: ')).lower
    if picture == 'no':
        print(f'Your total bill is £{bill}')
    else:
        Total_bill = bill + 3
        print(f'Your total bill is £{Total_bill}')
        
else:
    print('Sorry, you have to grow taller before you can ride.')
    

#dirty_dozen =['Strawberries', 'Spinach', 'Kale', 'Nectarines', 'Apples', 'Grapes', 'Cherries', 'Peaches', 'Pears', 'Bell peppers', 'Celery', 'Tomatoes']

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Cherries', 'Peaches', 'Pears', 'Tomatoes']
vegetables = ['Spinach', 'Kale', 'Bell peppers', 'Celery']

dirty_dozen = [fruits, vegetables] # a way to create a nested list (a list within a list)
print(dirty_dozen[1][1]) # this will print kale which is the second item in the second list
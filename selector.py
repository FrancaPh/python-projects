
import random

friends = [
    'Luana',
    'Brenda',
    'Daniel',
    'Matheus',
    'Carla',
    'Marcos',
    'Alex',
    'Gabrielle',
    'Nadya'
]

# random.choice(array) --> random item in this array

selected = random.choice(friends) # randomly choose a friend

print('Who should I facetime today?')
print(selected)
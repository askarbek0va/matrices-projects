import os
import random
name=input('Please enter your name:')
print('Now we are starting to play')
print("A B C D E F G")
a = [['o'] * 7 for i in range(7)] 
for row in a:
    print(' '.join(row))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ships_location():
    ships = []
    for ship_size in [3, 2, 2, 1, 1, 1, 1]:
        ship_coordinates = ships_location(ship_size, ships)
        ships.extend(ship_coordinates)
    return ships


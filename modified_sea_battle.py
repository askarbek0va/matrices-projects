import os
import random

def print_board(board):
     print("   A B C D E F G")
     for i, row in enumerate(board):
        print(f"{i} |{'|'.join(row)}|")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ships_location():
    ships = []
    for ship_size in [3, 2, 2, 1, 1, 1, 1]:
        ship_coordinates = place_ship(ship_size, ships)
        ships.extend(ship_coordinates)
    return ships
def place_ship(size, existing_ships):
    while True:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            x = random.randint(0, 6)
            y = random.randint(0, 6 - size)
            ship_coordinates = [(x, y + i) for i in range(size)]
        else:
            x = random.randint(0, 6 - size)
            y = random.randint(0, 6)
            ship_coordinates = [(x + i, y) for i in range(size)]

        if all(coord not in existing_ships for coord in ship_coordinates):
            break
    return ship_coordinates

def convert_input(input_str):
    try:
        y, x = input_str.upper()
        x = int(x)
        y = ord(y) - ord('A')
        return x,y
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid coordinate (e.g., A1).")
        return take_turn()
    
def take_turn():
    try:
        guess = input("Enter your guess (e.g., A1): ")
        x, y = convert_input(guess)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid coordinate (e.g., A1).")
        return take_turn()
    if not (0 <= x < 7 and 0 <= y < 7):
        print("Invalid coordinates. Please enter a valid coordinate.")
        return take_turn()

    return x, y

def update_board(board, x, y, result):
    if result == "miss":
        board[x][y] = '•'
    elif result == "hit":
        board[x][y] = 'X'
    elif result == "sunk":
        board[x][y] = '#'

def check_shot_result(x, y, ships):
    if (x, y) in ships:
        ships.remove((x, y))
        if not any(coord in ships for coord in get_adjacent_coordinates(x, y)):
            return "sunk"
        return "hit"
    return "miss"

def get_adjacent_coordinates(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def play():
    name=input('Please enter your name:')
    print('Now we are starting to play')
    ships=ships_location()
    board = [[' ' for i in range(7)] for i in range(7)]

    turns = 0
    while ships:
        clear_screen()
        print_board(board)
        x, y = take_turn()
        turns += 1

        result = check_shot_result(x, y, ships)
        update_board(board, x, y, result)

        if not ships:
            clear_screen()
            print_board(board)
            print(f"Congratulations, {name}! You sank all the ships in {turns} turns.")
            play_again()
def play_again():
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play()
    else:
        print("Game over. Here's the sorted list of players:" )
        # Add sorting logic for players (not implemented)
        exit()

if __name__ == "__main__":
    play()
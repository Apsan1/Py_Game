import numpy as np
import random
def player_name():
    print('Hello, Gamer!!')
    name = input('Enter Your Name: ')
    return name
def layout(grid):
    for i in range(4):
        x = random.randint(0,5)
        y = random.randint(0,5)
        grid[x,y] = i+1
    print(grid)

def player_move(grid):
    shots_left = 6
    while shots_left > 0:
        print('You have',shots_left,'shots left. !!')
        row = int(input('\nEnter the row:'))
        col = int(input('\nEnter the column: '))
        if grid[row,col] == 0:
            print('\nMiss')
        elif grid[row,col] == 1:
            print('\nHit')
            grid[row,col] = 0
        elif grid[row,col] == 2:
            print('\nHit')
            grid[row,col] = 0
        elif grid[row,col] == 3:
            print('\nHit')
            grid[row,col] = 0
        elif grid[row,col] == 4:
            print('\nHit')
            grid[row,col] = 0
        else:
            print('\nError')
        shots_left = shots_left - 1
        print(grid)
def run_game():
    p_name = player_name()
    grid = np.zeros((6,6))
    print('\nWelcome to Battleships ', p_name)
    print('\nThis is the area we are going to battle on:')
    layout(grid)
    print('\nThese are the enemy vehicles intels: ')
    print("\n1 = ‘Battleship' \n2 = ‘Aircraft Carrier' \n3 = ‘Submarine' \n4 = ‘Destroyer’")
    print('\nSelect an area to shoot!!\n')
    player_move(grid)
run_game()

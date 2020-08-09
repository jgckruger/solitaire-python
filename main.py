from classes.Game import Game
import os
import time

clear = lambda: os.system('cls')

game = Game()
while(not(game.check_for_end())):
    clear()
    print(game)
    action = input()
    game.command(action)
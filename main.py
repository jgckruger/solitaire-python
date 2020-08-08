from classes.Game import Game
import os
import time

clear = lambda: os.system('cls')

game = Game()
game.print_status()

while(not(game.check_for_end())):
    # clear()
    game.print_status()
    action = input()
    game.command(action)
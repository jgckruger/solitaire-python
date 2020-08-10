from classes.Game import Game
import os
import time

game = Game()
game.help()

while(not(game.check_for_end())):
    game.clear_screen()
    print(game)
    action = input()
    game.command(action)

print("You win")

from random import shuffle
from classes.Card import Card
from classes.Hand import Hand
from classes.Pile import Pile
from classes.Deck import Deck
from classes.Table import Table
from classes.Foundation import Foundation
import os

class Game:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.deck = self.generate_new_deck()
        self.hand = self.generate_new_hand()
        self.foundations = self.generate_new_foundations()
        self.piles = self.generate_new_piles()
        self.table = self.generate_new_table()

    def generate_new_deck(self):
        cards = []
        # generates new Deck
        for i in range(4):      # cards
            for j in range(13):  # suits
                cards.append(Card(j, i))

        deck = Deck(cards)
        deck.shuffle()
        return deck

    def generate_new_foundations(self):
        foundations = []
        for i in range(4):
            foundations.append(Foundation(i))
        return foundations

    def generate_new_piles(self):
        piles = []
        for i in range(7):
            pile = Pile(self.deck.slice_deck(i+1))
            piles.append(pile)

        return piles

    def generate_new_table(self):
        table = Table(self.deck, self.hand, self.piles, self.foundations)
        return table

    def generate_new_hand(self):
        hand = Hand([])
        return hand

    def check_for_end(self):
        for foundation in self.foundations:
            if not(foundation.is_full()):
                return False
        return True

    def print_status(self):
        self.table.print_table()

    def __str__(self):
        return str(self.table)

    def draw(self):
        top_card = self.deck.pop_card()
        print(top_card)
        if(top_card):
            top_card.turn_card()
            self.hand.insert_card(top_card)
            return True
        self.deck = Deck(self.hand.get_hand())
        self.hand = Hand([])
        return True

    def move(self, action):
        try:
            if action[1] == "H":
                # Move to Foundation
                card = self.hand.top()
                if action[2] == "F":
                    suit = card.suit
                    if(self.foundations[suit].insert_card(card)):
                        self.hand.pop_card()
                # Move to Pile X
                if(action[2] == "P"):
                    column = int(action[3])
                    if(self.piles[column].insert_cards([card])):
                        self.hand.pop_card()
            # Move from Pile
            elif action[1] == "P":
                column = int(action[2])
                # Move to Foundation
                if action[3] == "F":
                    card = self.piles[column].top()
                    suit = card.suit
                    if(self.foundations[suit].insert_card(card)):
                        self.piles[column].remove(-1)
                # Move to Pile
                elif action[3] == "P":
                    columnY = int(action[4])
                    n_cards = int(action[6:] or 1)
                    cards = self.piles[column].top_n(-n_cards)
                    if(self.piles[columnY].insert_cards(cards)):
                        self.piles[column].remove(-n_cards)
            # Move from Foundation
            elif action[1] == "F":
                columnX = int(action[2])
                card = self.foundations[columnX].top()
                # Move to Pile
                if action[3] == "P":
                    columnY = int(action[4])
                    if(self.piles[columnY].insert_cards([card])):
                        self.foundations[columnX].pop_card()
        except:
            print("Invalid Movement")

    def help(self):
        self.clear_screen()
        print("# Welcome to Solitaire")
        print("Commands")
        print("# Show Commands : H")
        print("# Reset Game : N")
        print("# Draw Card : D")
        print("# Move Card : ")
        print("     # Hand to Foundation : MHF")
        print("     # Hand to Pile : MHPX")
        print("     # Pile X to Foundation : MPXF")
        print("     # Move Pile X to Pile Y, Z cards : MPXPYNZ")
        print("     # If Z is not provided, it will try movement with 1 card")
        print("     # Move Foundation X to Pile Y : MFXPY")
        print("Press Any Key to Start or Resume Game")
        input()

    def command(self, action):
        # No Action
        if len(action) == 0:
            return False
        action = action.upper()
        if(action[0] == "H"):
            self.help()
        # Draw Card
        if(action[0] == "D"):
            self.draw()
        # Move Card
        elif action[0] == "M":
            self.move(action)
        # New Game
        elif action[0] == "N":
            self.start_game()

        # Change Board State
        self.table.deck = self.deck
        self.table.hand = self.hand
        self.table.foundations = self.foundations
        self.table.piles = self.piles
        return True

    def clear_screen(self):
        return os.system('cls')
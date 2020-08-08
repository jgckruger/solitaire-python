from random import shuffle
from classes.Card import Card
from classes.Hand import Hand
from classes.Pile import Pile
from classes.Deck import Deck
from classes.Table import Table
from classes.Foundation import Foundation


class Game:
    def __init__(self):
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
        
    def command(self, action):
        if len(action) == 0:
            print("Nope")
            return False
        # Draw Card
        if action[0] == "D":
            top_card = self.deck.pop_card()
            if(top_card):
                top_card.turn_card()
                self.hand.insert_card(top_card)
                return True

            self.deck = Deck(self.hand.get_hand())
            self.hand = Hand([])
            
            return True

        # Move Card
        # Move Hand to Foundation OK
            # MHF
        # Move Hand to Pile OK
            # MHPX
        # Move Pile X to Foundation Y
            # MPXF
        # Move Pile X to Pile Y
            # MPXPYN

        elif action[0] == "M":
            # Move from Hand
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
                if action[3] == "F":
                    card = self.piles[column].top()
                    suit = card.suit
                    if(self.foundations[suit].insert_card(card)):
                        self.piles[column].remove(1)


        self.table.deck = self.deck
        self.table.hand = self.hand
        self.table.foundations = self.foundations
        self.table.piles = self.piles

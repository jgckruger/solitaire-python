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


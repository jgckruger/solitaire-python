from random import shuffle
from classes.Card import Card
from classes.Hand import Hand
from classes.Pile import Pile
from classes.Deck import Deck
from classes.Foundation import Foundation


class Game:
    def __init__(self):
        self.deck = self.generate_new_deck()
        self.foundations = self.generate_new_foundations()

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

    def check_for_end(self):
        for foundation in self.foundations:
            if not(foundation.is_full()):
                return False
        return True


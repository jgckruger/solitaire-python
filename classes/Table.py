from classes.Card import Card
from classes.Hand import Hand
from classes.Pile import Pile
from classes.Deck import Deck
from classes.Foundation import Foundation

class Table:
    def __init__(self, deck, hand, piles, foundations):
        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.foundations = foundations

    def check_for_end(self):
        for foundation in self.foundations:
            if not(foundation.is_full()):
                return False
        return True 

    def print_table(self):
        print('Deck: ', len(self.deck))
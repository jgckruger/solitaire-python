from random import shuffle
from classes.Card import Card

class Deck:
    cards = []

    def __init__(self, cards):
        self.cards = [card.to_face_down() for card in cards]

    def shuffle(self):
        shuffle(self.cards)
        shuffle(self.cards)
        shuffle(self.cards)

    def pop_card(self):
        if(len(self.cards)):
            return self.cards.pop()
        return False
    
    def print(self):
        for card in self.cards:
            print(card)

    def __len__(self):
        return len(self.cards)
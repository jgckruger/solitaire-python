from random import shuffle
from classes.Card import Card
from classes.Color import Color

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
        return None

    def print(self):
        for card in self.cards:
            print(card)
    
    def slice_deck(self, n):
        # TODO: check implementation
        if len(self.cards) == 0:
            return None
        card_list = self.cards[:n]
        del self.cards[:n]
        return card_list

    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        if len(self):
            return Color.FACE_DOWN + '[' + str(len(self)).zfill(2) + ' ]' + Color.RESET
        return Color.EMPTY + '[ X ]' + Color.RESET

    def __repr__(self):
        if len(self):
            return '[' + str(len(self)).zfill(2) + ' ]'
        return '[ X ]'
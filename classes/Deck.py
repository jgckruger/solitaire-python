from classes.Card import Card

class Deck:

    cards = None

    def __init__(self, cards, from_hand = False):
        if(from_hand):
            self.cards = [card.turn_card() for card in cards]
        else:
            self.cards = cards

    def pop_card(self):
        if(len(self.cards)):
            return self.cards.pop()
        else:
            return False
    
    def print(self):
        for card in self.cards:
            print(card.get_card_values())
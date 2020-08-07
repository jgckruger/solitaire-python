from classes.Card import Card

class Deck:
    cards = None

    def __init__(self, cards):
        self.cards = [card.to_face_down() for card in cards]

    def pop_card(self):
        if(len(self.cards)):
            return self.cards.pop()
        return False
    
    def print(self):
        for card in self.cards:
            print(card.get_card_values())
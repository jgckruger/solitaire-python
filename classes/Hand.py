from classes.Card import Card


class Hand:
    cards = None

    def __init__(self, cards):
        self.cards = []

    def pop_card(self):
        if(len(self.cards)):
            return self.cards.pop()
        else:
            return False

    def insert_card(self, card):
        self.cards.append(card)

    def clear_hand(self):
        self.cards = []

    def get_hand(self):
        return self.cards
    
    def top(self):
        if len(self.cards):
            return self.cards[-1]
        return None

    def __repr__(self):
        if not(self.top()):
            return '[ X ]'
        return str(self.top())

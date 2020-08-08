from classes.Card import Card

suit_names = ['♣', '♦', '♥', '♠']
colors = ['black', 'red', 'red', 'black']

class Foundation:
    def __init__(self, suit):
        self.cards = []   # STACK
        self.suit = suit
        self.suit_str = suit_names[suit]
        self.color = colors[suit]

    def validate_card_into_foundation(self, card: Card):
        # Checks if the suit is the same
        if card.suit != self.suit:
            return False
        
        # Check if the card value is the same as the 
        if len(self.cards) != card.value:
            return False
        return True

    def insert_card(self, card):
        # If it fails, return False
        if not(self.validate_card_into_foundation(card)):
            return False
        # Inserts card into deck
        self.cards.append(card)
        return True

    def top(self):
        if len(self.cards) == 0:
            return None
        # Returns last card
        return self.cards[-1]

    def is_full(self):
        if len(self.cards) == 13:
            return True
        return False

    def get_foundation_values(self):
        foundation = {
            'suit': self.suit,
            'suit_str': self.suit_str,
            'top_card': self.top(),
            'is_full': self.is_full()
        }

        return foundation

    def __repr__(self):
        if not(self.top()):
            return '[ X ]'
        return str(self.top())
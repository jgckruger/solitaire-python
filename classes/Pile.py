from classes.Card import Card


class Pile:

    cards = None

    def __init__(self, cards):
        self.cards = cards
        self.cards[-1].turn_card()

    def top(self):
        if len(self.cards):
            return self.cards[-1]
        return None
    
    def top_n(self, n):
        if len(self.cards):
            return self.cards[n:]
        return None

    def insert_cards(self, card_list):
        top_pile = self.top()
        first_card = card_list[0]
        if top_pile == None:
            if first_card.value == 12:  # K
                self.cards = card_list
                return True
            return False
        elif (first_card.color != top_pile.color) and (first_card.value + 1 == top_pile.value):
            self.cards = self.cards + card_list
            return True
        return False

    def remove(self, n):
        if len(self.cards) and self.cards[n].face_up:
            card_list = self.cards[n:]
            del self.cards[n:]
            if len(self.cards) and not(self.top().face_up):
                self.cards[-1].turn_card()
            return card_list
        return None

    def print(self):
        for card in self.cards:
            print(card)

    def get_card(self, row):
        if row + 1 > len(self.cards):
            return '     '
        return str(self.cards[row])

    # TODO: redo
    def __repr__(self):
        pile = []
        for card in self.cards:
            pile.append(str(card))
        return str(pile)+'\n'

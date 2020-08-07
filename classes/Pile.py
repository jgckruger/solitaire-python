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
    
    def insert_cards(card_list):
        top_pile = self.top()
        first_card = card_list[0]
        if top_pile == None:
            if first_card.value == 12: ## K
                self.cards = card_list
                return True
            return False
        elif (first_card.color != top_pile.color) and (first_card.value + 1 == top_pile.value):
            self.cards + card_list
            return True
        return False

    
class Table:
    def __init__(self, deck, hand, piles, foundations):
        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.foundations = foundations

    def print_table(self):
        print('Deck: ', len(self.deck))
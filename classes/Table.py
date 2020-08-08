class Table:
    def __init__(self, deck, hand, piles, foundations):
        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.foundations = foundations

    def print_table(self):
        print('Deck Len: ', len(self.deck))

        print(self.piles)
        print(self.foundations)
        print(self.hand)
        print(self.deck)
        
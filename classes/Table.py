##   D      H      0       1       2       3       4       5       6       F
#  [24 ]  [ X ]  [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                        [A S]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                                [A S]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                                        [A S]   [ D ]   [ D ]   [ D ]
#                                                [A S]   [ D ]   [ D ]
#                                                        [A S]   [ D ]
#                                                                [A S]

class Table:
    spacing = '   '
    header = [' D ', 'H', ' 0 ', ' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' F ']
    
    def __init__(self, deck, hand, piles, foundations):
        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.foundations = foundations

    def __str__(self):
        table = ''
        rows = []
        rows.append(self.header)
        for i in range(len(self.piles)):
            print(i)


        return table
    

    def generate_row(self, elements):
        row = ''
        for element in elements:
            row += element + self.spacing
        return row

    def print_table(self):
        print('Deck Len: ', len(self.deck))

        print(self.piles)
        print(self.foundations)
        print(self.hand)
        print(self.deck)
        
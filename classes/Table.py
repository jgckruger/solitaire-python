#     D       H       0       1       2       3       4       5       6       F
#   [24 ]   [ X ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                           [A S]   [ D ]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                                   [A S]   [ D ]   [ D ]   [ D ]   [ D ]   [ X ]
#                                           [A S]   [ D ]   [ D ]   [ D ]
#                                                   [A S]   [ D ]   [ D ]
#                                                           [A S]   [ D ]
#                                                                   [A S]

class Table:
    spacing = '   '
    header = ['  D  ', '  H  ', '  0  ', '  1  ', '  2  ', '  3  ', '  4  ', '  5  ', '  6  ', '  F  ']
    
    def __init__(self, deck, hand, piles, foundations):
        self.deck = deck
        self.hand = hand
        self.piles = piles
        self.foundations = foundations
        self.empty_row = ['     ' for _ in range(10)]

    def __str__(self):
        table = ''
        rows = []
        rows.append(self.header)
        for i in range(20):
            row = []

            # adds deck to first line
            if i == 0:
                row += [str(self.deck), str(self.hand)]
            else:
                row += ['     ', '     ']


            # adds card or empty space for each possible position in the pile
            for pile in self.piles:
                row.append(pile.get_card(i))
            

            # checks if foundation has to be added
            if i < 4:
                row.append(str(self.foundations[i]))
            else:
                row.append('     ')


            rows.append(row) 

        rows = [row for row in rows if row != self.empty_row]

        for row in rows:
            row_str = self.generate_row(row)
            table += row_str

        return table
    

    def generate_row(self, elements):
        row = ''
        for element in elements:
            row += element + self.spacing
        row += '\n'
        return row

    def print_table(self):
        print('Deck Len: ', len(self.deck))

        print(self.piles)
        print(self.foundations)
        print(self.hand)
        print(self.deck)
        
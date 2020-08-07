card_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suit_names = ['♣', '♦', '♥', '♠']
colors = ['black', 'red', 'red', 'black']

class Card:
    value = None
    str_val = None
    suit = None
    color = None
    face_up = False

    def __init__(self, value, suit, face_up = False):
        # TODO: Force value to exist within predetermined range
        self.value = value
        self.suit = suit
        self.face_up = face_up

        self.str_val = card_names[value]
        self.suit_name = suit_names[suit]
        self.color = colors[suit]        

    def turn_card(self):
        self.face_up = not(self.face_up)

    def to_face_down(self):
        self.face_up = False
        return self

    def get_card_values(self):
        card = {
            'value': self.value,
            'suit': self.suit,
            'face_up': self.face_up,
            'str_val': self.str_val,
            'suit_name': self.suit_name,
            'color': self.color
        }

        return card
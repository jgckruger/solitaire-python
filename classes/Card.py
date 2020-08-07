class Card:
    value = None
    str_val = None
    suit = None
    color = None
    face_up = False

    def __init__(self, value, suit, color, face_up = False):
        # TODO: Force value to exist within predetermined range
        self.value = value
        self.suit = suit
        self.color = color
        self.face_up = face_up

    def turn_card(self):
        self.face_up = not(self.face_up)
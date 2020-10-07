class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # good practice is to include repr and str magic methods - that way you can print meaningful info
    def __repr__(self):
        return '<{} {}>'.format(self.value, self.suit)

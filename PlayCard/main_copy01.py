from collections import deque
from utils import game_main01
import random


#class Card: is moved to the utils folder
#    def __init__(self, suit, val):
#        self.suit = suit
#        self.value = val

    # good practice is to include repr and str magic methods - in order to be abe to print info
#    def __repr__(self):
#        return '<{} {}>'.format(self.value, self.suit)


class Deck: #this class makes the deck with 52 cards to choose from
    def __init__(self):
        # use deque - it's more efficient to pop from left than from a list
        self.cards = deque()
        self.build()

    def build(self):
        self.cards.clear()
        for i in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for j in range(1, 14):
                self.cards.append(game_main01.Card(i, j))
        # need to shuffle in order to have random order of cards
        random.shuffle(self.cards)

    def length(self):
        return len(self.cards)

    def get_card(self):
        return self.cards.popleft()

    def __repr__(self):
        return 'Deck: [{} Cards]'.format(self.length())


class Game: # gives to every player 10 cards, unless there are not that much available yet. 52 divided by 6 doesn't return an integer
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.counter = 0

    def deal(self):
        for player in self.players:
            for i in range(10):
                player.give_card(self.draw_card())
                self.counter += 1
                if self.counter == 52:
                    break
    # in python use underscore not camelCase for methods
    def draw_card(self):
        # avoid mutating other object properties in other objects
        return self.deck.get_card()

    def restart_game(self):
        # simply rebuild the deck - it will reshuffle all cards
        self.deck.build()
        for player in self.players:
            player.return_cards()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def give_card(self, card):
        self.cards.append(card)

    def return_cards(self):
        self.cards = []

    def __repr__(self):
        return 'Player: {} - [{}]'.format(self.name, ','.join([str(x) for x in self.cards]))


deck_of_cards = Deck()
player_one = Player("John")
player_two = Player("Harrry")
player_three = Player("Sucy")
player_four = Player("Benji")
player_five = Player("Kenji")
player_six = Player("Anny")
new_game = Game([player_one, player_two, player_three, player_four, player_five, player_six], deck_of_cards)
new_game.deal()
print(player_one, player_two, player_three, player_four, player_five, player_six)
print(new_game.deck)
new_game.restart_game()
print(player_one, player_two, player_three, player_four, player_five, player_six)
print(new_game.deck)
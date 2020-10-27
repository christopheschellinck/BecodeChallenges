from collections import deque
from utils import game
import random


class Deck: #this class makes the deck with 52 cards to choose from
    def __init__(self):
        # deque - is to (read an item via popleft) from left
        self.cards = deque()
        self.build()

    def build(self):
        self.cards.clear()
        for i in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for j in range(1, 14):
                self.cards.append(game.Card(i, j))
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
                if self.counter == 51:
                    break

    def draw_card(self):
        return self.deck.get_card()

    def restart_game(self):
        # rebuild the deck - it will reshuffle all cards
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
player_one = Player("Mary")
player_two = Player("Jude")
player_three = Player("dentist")
player_four = Player("hairdresser")
player_five = Player("occupy")
player_six = Player("Elvis")
new_game = Game([player_one, player_two, player_three, player_four, player_five, player_six], deck_of_cards)
new_game.deal()
print(player_one, player_two, player_three, player_four, player_five, player_six)
print(new_game.deck)

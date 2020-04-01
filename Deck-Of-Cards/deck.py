from random import shuffle
from .card import Card

class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = [Card(suit, value) for value in Deck.values for suit in Deck.suits]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        cards_dealt = []
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() < num:
            for i in range(self.count()):
                cards_dealt.append(self.cards.pop())
            return cards_dealt
        else:
            for i in range(num):
                cards_dealt.append(self.cards.pop())
            return cards_dealt

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


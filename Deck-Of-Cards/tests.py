import unittest
from .card import Card
from .deck import Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Diamonds", "A")

    def test_init(self):
        self.assertEqual(self.card.suit, "Diamonds")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        self.assertEqual(repr(self.card), "A of Diamonds")


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        self.assertIsInstance(self.deck.cards, list)
        self.assertEqual(self.deck.count(), 52)

    def test_repr(self):
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_iter(self):
        self.assertTrue(iter(self.deck), isinstance(self.deck, list))

    def test_count(self):
        self.assertTrue(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertTrue(self.deck.count(), 51)

    def test_deal_empty(self):
        with self.assertRaises(ValueError):
            self.deck.cards = []
            self.deck._deal(1)

    def test_deal_sufficient_cards(self):
        cards = self.deck._deal(3)
        self.assertEqual(len(cards), 3)
        self.assertEqual(self.deck.count(), 49)

    def test_deal_insufficient_cards(self):
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_shuffle_notfull(self):
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            self.deck.shuffle()

    def test_shuffle(self):
        shuffled_deck = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, shuffled_deck)
        self.assertEqual(self.deck.count(), 52)

    def test_deal_card(self):
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

if __name__ == "__main__":
    unittest.main()

import unittest
from Deck import Deck
import FLAGS
from Player import Player
from Run import GetSumOfCards

ERROR_FLAG = -1
SUCCESS = True
BUSTED = -2
LOST = -3
WIN = 1
CARD_CATEGORY = ["Hearts", "Spades", "Diamond", "Clubs"]
INSUFFICIENT_CHIPS = -4
CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class TestBlackJack(unittest.TestCase):

    def test_player(self):
        player1 = Player("Sagar", 1000)
        result1 = player1.placebet(100)
        result2 = player1.placebet(1000)

        self.assertEqual(result1, SUCCESS)
        self.assertEqual(result2, INSUFFICIENT_CHIPS)

    def test_deck(self):
        mydeck = Deck()
        for i in range(1, 10):
            cardtuple = mydeck.drawcard()
            print(cardtuple)
            self.assertIn(cardtuple, mydeck.cards_drawn)

    def test_GetCardsSumation(self):
        cardsdrawn = [('4', "Hearts"), ('6', "Spades")]
        result = GetSumOfCards(cardsdrawn)
        print(result)
        self.assertEqual(result, 10)

if __name__ == '__main__':
        unittest.main()

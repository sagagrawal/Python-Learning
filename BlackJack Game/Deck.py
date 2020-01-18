import random as rd

ERROR_FLAG = -1
SUCCESS = True
BUSTED = -2
LOST = -3
WIN = 1
CARD_CATEGORY = ["Hearts", "Spades", "Diamond", "Clubs"]
INSUFFICIENT_CHIPS = -4
CARDS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    cards_drawn = []

    def __init__(self):
        pass

    def drawcard(self):
        while True:
            random_num = rd.choice(CARDS)
            random_category = rd.choice(CARD_CATEGORY)

            if len(self.cards_drawn) > 0:
                if not (random_num, random_category) in self.cards_drawn:
                    self.cards_drawn.append((random_num, random_category))
                    break
            else:
                self.cards_drawn.append((random_num, random_category))

        return random_num, random_category

    def GetSumOfCards(self, cards_drawn):

        resultsum = 0
        count = 0
        for card_no, category in cards_drawn:
            if not card_no.isnumeric():
                resultsum += 10
            elif card_no == '1':
                count += 1
            else:
                resultsum += int(card_no)
        if count > 0:
            if resultsum+(11*count) > 21:
                resultsum += count
            else:
                resultsum += (11*count)

        return resultsum


if __name__ == '__main__':
    mydeck = Deck()
    tuple = mydeck.drawcard()
    print(tuple)
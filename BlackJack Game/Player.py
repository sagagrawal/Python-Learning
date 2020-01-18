ERROR_FLAG = -1
SUCCESS = True
BUSTED = -2
LOST = -3
WIN = 1
CARD_CATEGORY = ["Hearts", "Spades", "Diamond", "Clubs"]
INSUFFICIENT_CHIPS = -4
CARDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Player:
    name = ""
    chips_in_hand = 0
    wins = 0
    lost = 0
    busted = 0

    def __init__(self, name="PLAYER", initial_chips=5000):
        self.name = name
        self.chips_in_hand = initial_chips

    def placebet(self, chips):
        if chips > self.chips_in_hand:
            return INSUFFICIENT_CHIPS
        else:
            self.chips_in_hand -= chips
            return SUCCESS

    def udpate_chips_balance(self, chips):
        if(chips > 0):
            self.chips_in_hand += chips
            return SUCCESS
        else:
            return ERROR_FLAG

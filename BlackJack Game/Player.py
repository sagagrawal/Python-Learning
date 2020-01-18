ERROR_FLAG = -1
SUCCESS = True
BUSTED = -2
LOST = -3
WIN = 1
INSUFFICIENT_CHIPS = False


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
        if chips > self.chips_in_hand or chips < 500:
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

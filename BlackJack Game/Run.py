from PrintHelper import print_table
import time
from Deck import Deck
from colorama import Fore
from colorama import init

DEALER_WINS = 1
DEALER_BUSTED = -1
PLAYER_WINS = 2
PLAYER_BUSTED = -2
GAME_ON = 3
play_status = True
game_deck = Deck()
player_cards_drawn = []
dealer_cards_drawn = []

init()


def generate_result():
    dealer_result = game_deck.GetSumOfCards(dealer_cards_drawn)
    player_result = game_deck.GetSumOfCards(player_cards_drawn)

    if dealer_result <= 21:
        if dealer_result > player_result and not play_status:
            return DEALER_WINS
        elif player_result > 21:
            return DEALER_WINS
    else:
        return DEALER_BUSTED

    if player_result <= 21:
        if dealer_result < player_result and not play_status:
            return PLAYER_WINS
        elif dealer_result > 21:
            return PLAYER_WINS
    else:
        return PLAYER_BUSTED

    return GAME_ON


def LetsPlay():
    global play_status
    global player_cards_drawn
    global dealer_cards_drawn
    global game_deck
    flag = True
    game_result = GAME_ON

    while flag:
        # clear_output()
        print("Welcome to BLACK-JACK command line GAME!!")
        print("Drawing 2 cards for PLAYER and 1 card for HOUSE....")
        time.sleep(3)

        player_cards_drawn.append(game_deck.drawcard())
        player_cards_drawn.append(game_deck.drawcard())

        dealer_cards_drawn.append(game_deck.drawcard())

        print_table(play_status, dealer_cards_drawn, player_cards_drawn, game_deck)

        player_choice = True
        count = 1
        while player_choice:
            print("\n1. Hit\n2. Stay\nInput your Choice(input 1 or 2): ")
            if int(input()) == 1:
                player_cards_drawn.append(game_deck.drawcard())
                game_result = generate_result()
                if game_result == GAME_ON:
                    # clear_output()
                    print_table(play_status, dealer_cards_drawn, player_cards_drawn, game_deck)
                    count += 1
                else:
                    play_status = False
                    break
            else:
                play_status = False
                player_choice = False

        if game_result == GAME_ON:
            print("Now, Drawing cards for HOUSE....")
            time.sleep(5)
            for _ in range(1, count+1):
                dealer_cards_drawn.append(game_deck.drawcard())
                # clear_output()
                print_table(play_status, dealer_cards_drawn, player_cards_drawn, game_deck)

            play_status = False
        # clear_output()
        print_table(play_status, dealer_cards_drawn, player_cards_drawn, game_deck)

        flag = False


if __name__ == '__main__':
    LetsPlay()
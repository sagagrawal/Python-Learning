from colorama import init
from colorama import Fore
from Deck import Deck


DEALER_WINS = 1
DEALER_BUSTED = -1
PLAYER_WINS = 2
PLAYER_BUSTED = -2
GAME_ON = 3

init()


def print_cards(cards_drawn):
    '''
    This method expects a tuple list of cards drawn
    '''

    print_horizontal_line(cards_drawn)

    for i, (card_no, category) in enumerate(cards_drawn):
        if i == len(cards_drawn) - 1:
            print(f"| {category[0]}  |    ")
        else:
            print(f"| {category[0]}  |    ", end=" ")

    for i, (card_no, category) in enumerate(cards_drawn):
        if i == len(cards_drawn) - 1:
            print(f"|  {card_no} |    ")
        else:
            print(f"|  {card_no} |    ", end=" ")

    print_horizontal_line(cards_drawn)


def print_horizontal_line(cards_drawn):
    for i, (card_no, category) in enumerate(cards_drawn):
        if i == len(cards_drawn) - 1:
            print("------    ")
        else:
            print("------    ", end=" ")


def print_table(play_status, dealer_cards_drawn, player_cards_drawn, game_deck, chips_on_bet, human_player):

    # clear_output()
    print("\n****************************************")
    print("                 DEALER                 ")
    print("****************************************")

    print_cards(dealer_cards_drawn)
    dealer_result = game_deck.GetSumOfCards(dealer_cards_drawn)
    player_result = game_deck.GetSumOfCards(player_cards_drawn)

    print(Fore.CYAN + f"\t\t\t\t\tDealer Total: {dealer_result}", end=" " + Fore.RESET)

    if not play_status:
        if dealer_result <= 21:
            if dealer_result > player_result or player_result > 21:
                print(Fore.GREEN + "HOUSE WINS" + Fore.RESET)
        else:
            print(Fore.RED + "BUSTED" + Fore.RESET)
            human_player.chips_in_hand += (2*chips_on_bet)

    print("")

    print(Fore.CYAN + f"\t\t\t\t\tPlayer Total: {player_result}", end=" " + Fore.RESET)
    if not play_status:
        if player_result <= 21:
            if dealer_result < player_result or dealer_result > 21:
                print(Fore.GREEN + "PLAYER WINS" + Fore.RESET)
                human_player.chips_in_hand += (2 * chips_on_bet)
        else:
            print(Fore.RED + "BUSTED" + Fore.RESET)

    print("")
    print_cards(player_cards_drawn)

    if not play_status:
        chips_on_bet = " - "

    print("****************************************          " + Fore.RED + f"Chips on Bet: {chips_on_bet}" + Fore.RESET)
    print("                 PLAYER                 ")
    print("****************************************          " + Fore.BLUE + f"Chips in Hand: {human_player.chips_in_hand}" + Fore.RESET)

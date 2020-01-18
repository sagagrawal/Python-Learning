from random import randint
from IPython.display import clear_output

ERROR_FLAG = -1
POSITIONAL_BOARD = ["1", "2", "3",
                    "4", "5", "6",
                    "7", "8", "9"]
whoseturn = True


def print_board(board=POSITIONAL_BOARD):
    if len(board) == 9:
        for x in range(0, 3):
            print(f" {board[x*3]} | {board[x*3+1]} | {board[x*3+2]} ")
            if x in [0, 1]:
                print("-----------")
    else:
        return ERROR_FLAG


def input_from_user(key):
    ch = -1
    flag = False
    while not flag:
        inp = input(f"Enter the Position you wish to place your '{key}' at: ")
        if not inp.isnumeric():
            print("INVALID INPUT, please Try Again!")
        else:
            ch = int(inp)
            if not ch in range(1, 10):
                print("INVALID INPUT, please Try Again!")
            elif User_Board[ch-1] == 'O' or User_Board[ch-1] == 'X':
                print("INVALID INPUT, please Try Again!")
            else:
                flag = True
    return ch


def update_board(pos, key):
    User_Board[pos-1] = key


def check_play_status():
    return not (User_Board.count('O') + User_Board.count('X')) == 9


def check_game_result():
    if User_Board[0] == User_Board[1] == User_Board[2]:
        return User_Board[0]
    elif User_Board[3] == User_Board[4] == User_Board[5]:
        return User_Board[3]
    elif User_Board[6] == User_Board[7] == User_Board[8]:
        return User_Board[6]
    elif User_Board[0] == User_Board[3] == User_Board[6]:
        return User_Board[0]
    elif User_Board[1] == User_Board[4] == User_Board[7]:
        return User_Board[1]
    elif User_Board[2] == User_Board[5] == User_Board[8]:
        return User_Board[2]
    elif User_Board[0] == User_Board[4] == User_Board[8]:
        return User_Board[0]
    elif User_Board[2] == User_Board[4] == User_Board[6]:
        return User_Board[2]
    else:
        return False


def select_player_randomly():
    random_player = randint(0, 1)
    global whoseturn
    whoseturn = (random_player == 1)
    if whoseturn:
        return 'X'
    else:
        return 'O'


while True:
    User_Board = list("         ")
    clear_output()
    print("Welcome to Tic Tac Toe Game")
    print(f"Key for Player 1 is: X")
    print(f"Key for Player 2 is: O")
    print(f"Player with Marker '{select_player_randomly()}' has been chosen randomly to go first!")
    print("Refer below Board to input the position you wish to place your key at, during your turn to PLAY!!!")
    print_board()

    while check_play_status():
        choice = -1
        if whoseturn:
            choice = input_from_user('X')
            update_board(choice, 'X')
            whoseturn = False
        else:
            choice = input_from_user('O')
            update_board(choice, 'O')
            whoseturn = True

        clear_output()
        print_board(User_Board)

    result = check_game_result()
    if type(result) == bool:
        print("GAME DRAW! Try Again")
    else:
        print(f"Congratulations!! Game won by Player having marker '{result}'")

    if not input("Wanna Play Again(y/n): ").lower() == "y":
        print("Quiting Tic Tac Toe Game...")
        break

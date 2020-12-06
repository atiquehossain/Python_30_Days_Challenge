#board
#display board
#play game
#handle turn
#check win
    #check row
    #check columns
    #check diagonals
#check tie
#flip player


board =["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going=True

winner=None

current_player="X"

def display_board():
    print(board[0] +" | " +board[1]+ " | " +board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    #board display
    display_board()

    while game_still_going:

        handle_turn(current_player)
        check_if_game_over()

        flip_player()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    #check row
    #check column
    # check diagonals
    return

def check_if_tie():
    return

def flip_player():
    return





def handle_turn(player):
    position= input("Choose a position from one to nine :\n")

    position=int(position)-1

    board[position]="X"
    display_board()

play_game()

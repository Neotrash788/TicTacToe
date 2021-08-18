# Declaring variables

# Empty board
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-"
]

turn = 'X'
run = True
winner = ""

# Game functions

# Displays board


def display_board():
    print(f''' |-----|-----|-----|
 |  {board[0]}  |  {board[1]}  |  {board[2]}  |
 |_____|_____|_____|
 |     |     |     |
 |  {board[3]}  |  {board[4]}  |  {board[5]}  |
 |_____|_____|_____|
 |     |     |     |
 |  {board[6]}  |  {board[7]}  |  {board[8]}  |
 |_____|_____|_____|''')
# Changes turn


def change_turn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

# Handles turn


def handle_turn(position):
    if board[position] in ['X', 'O']:
        print('Square is already occupied.')
        handle_turn(int(input(f'\n{turn} Choose a different square -> '))-1)
    else:
        board[position] = turn
        change_turn()


def check_for_winner():
    if check_rows():
        return True
    if check_columns():
        return True
    if check_diagonals():
        return True


winner_state = []


def check_rows():
    global winner, winner_state
    if board[0:3] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[0]
        winner_state = [0, 1, 2]
        return True
    elif board[3:6] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[3]
        winner_state = [3, 4, 5]
        return True
    elif board[6:9] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[6]
        winner_state = [6, 7, 8]
        return True


def check_columns():
    global winner, winner_state
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        winner_state = [0, 3, 6]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        winner_state = [1, 4, 7]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        winner_state = [2, 5, 8]
        return True


def check_diagonals():
    global winner, winner_state
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        winner_state = [0, 4, 8]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '-':
        winner = board[2]
        winner_state = [2, 4, 6]
        return True

# issue


def check_if_game_over():

    for square in board:
        if square == '-':
            return False
    else:
        return True


def display_winning_state():
    global board, winner
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    for i in range(len(winner_state)):
        board[winner_state[i]] = winner
    display_board()


def play_game():
    global run, board
    display_board()
    handle_turn(int(input(f"{turn}'s turn -> "))-1)

    if check_for_winner():
        run = False
        display_board()
        print(' <----------------->')
        display_winning_state()
        print(f"{winner} won!")
    else:
        if check_if_game_over():
            run = False
            display_board()
            print("Tie")


def run_game():
    while run:
        try:
            play_game()
        except IndexError:
            print('\nNumber must be between 1-9\n')
        except ValueError:
            print('\nInput must be an integer between 1-9\n')


run_game()


play_again = input("Play again? ").lower()
if play_again in ('y', 'yes', 'ye', 'yup'):
    run = True
    board = board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
    ]
    run_game()
else:
    quit()

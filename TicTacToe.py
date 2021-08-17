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
    print(' | '.join(board[0:3]))
    print('--+---+--')
    print(' | '.join(board[3:6]))
    print('--+---+--')
    print(' | '.join(board[6:9]))

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


def check_rows():
    global winner
    if board[0:3] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[0]
        return True
    elif board[3:6] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[3]
        return True
    elif board[6:9] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[6]
        return True


def check_columns():
    global winner
    if board[0] == board[3] == board[6] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[2]
        return True


def check_diagonals():
    global winner
    if board[0] == board[4] == board[8] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] in (["X", "X", "X"], ["O", "O", "O"]):
        winner = board[2]
        return True

# issue


def check_if_game_over():

    for square in board:
        if square == '-':
            return False
    else:
        return True


def play_game():
    global run
    display_board()
    handle_turn(int(input(f"\n{turn}'s turn -> "))-1)

    if check_for_winner():
        run = False
        print(f"{winner} won!")
    else:
        if check_if_game_over():
            run = False
            print("Tie")


while run:
    play_game()
input('Press Enter To End')

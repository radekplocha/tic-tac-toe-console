board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

player1 = 'X'
player2 = 'O'
game_is_in_progress = True
turn = 1
game_round = 1


def draw_board(b):
    for row in b:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if board.index(row) != 2:
            print("-----------")


def check_for_choice(b, ch):
    for row in b:
        for num in row:
            if num == ch:
                return row.index(num), board.index(row)


def check_for_win(b):
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    if board[1][0] == board[1][1] == board[1][2]:
        return True
    if board[2][0] == board[2][1] == board[2][2]:
        return True
    if board[0][0] == board[1][0] == board[2][0]:
        return True
    if board[0][1] == board[1][1] == board[2][1]:
        return True
    if board[0][2] == board[1][2] == board[2][2]:
        return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] == board[1][1] == board[2][0]:
        return True


def change_turn(t):
    if t == 2:
        return 1
    else:
        return 2


while game_is_in_progress:
    print('\n' * 5)
    draw_board(board)

    choice = input(f"PLAYER{turn} choose a place: ")
    try:
        x, y = check_for_choice(board, int(choice))
    except:
        continue

    board[y][x] = globals()[f'player{turn}']

    if game_round == 9 and not check_for_win(board):
        print('\n' * 5)
        print("DRAW")
        game_is_in_progress = False
        break
    if check_for_win(board):
        print('\n' * 5)
        print(f'PLAYER{turn} WON')
        game_is_in_progress = False
        break
    turn = change_turn(turn)
    game_round += 1

draw_board(board)
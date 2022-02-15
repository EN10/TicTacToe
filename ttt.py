board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-']]

def play_turn():
    x = int(input("x 0-2: "))
    y = int(input("y 0-2: "))
    try:
        if board[x][y] == '-':
            board[x][y] = 'O'
        else:
            play_turn()
    except IndexError:
        play_turn()

def check_win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'O' or \
           board[0][i] == board[1][i] == board[2][i] == 'O':     # cols
               print('win')
    if board[0][0] == board[1][1] == board[2][2] == 'O' \
    or board[0][2] == board[1][1] == board[2][0] == 'O':
        print('win')

for i in range(9):
    play_turn()
    check_win()
    for i in board:
        print(i)

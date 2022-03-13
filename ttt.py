import random

board = [ [' ',' ',' '] ,
          [' ',' ',' '] ,
          [' ',' ',' '] ]

def pc_plays():
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] == ' ':
        board[row][col] = 'O'
    else:
        pc_plays()

def displayboard():
    print('    0    1    2 ')
    for i in range(3):
        print (i, board[i])

def checkwinner(msg):
    for i in range(3):  # rows & cols
        if (board[i][0] == board[i][1] == board[i][2] and board[i][1] != ' ') \
        or (board[0][i] == board[1][i] == board[2][i] and board[1][i] != ' '):
               print(msg)
               return 'stop'
    if (board[0][0] == board[1][1] == board[2][2] and board[1][1] != ' ') \
    or (board[0][2] == board[1][1] == board[2][0] and board[1][1] != ' '):
        print(msg)
        return 'stop'

    hashes = 0
    for row in range (3):
        for col in range (3):
            if board[row][col] == ' ':
                hashes = hashes + 1
    if hashes == 0:
        print('Its a Draw!')
        return 'stop'

def userplays():
    try:
        row = int(input('row: '))
        col = int(input('column: '))
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print ('Cant play there!')
            userplays()
    except:
        print ('input either 0, 1 or 2')
        userplays()

while True:
    pc_plays()
    displayboard()
    if checkwinner('You Lose!') == 'stop':
        break

    quit = input('give up, type "yes" or press enter ')
    if quit == 'yes':
        break

    userplays()
    if checkwinner('You Win!') == 'stop':
        displayboard()
        break

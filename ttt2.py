# This program creates empty board with # then computer plays first "O" and human player with "X"
import random

# create empty board
board = [ ['#','#','#'] ,
          ['#','#','#'] ,
          ['#','#','#'] ]

#computer tries to find a hash randomly and if he cant then it tries again until it find it.
def computer_ai_plays():
    rrow= random.randint(0, 2)
    rcol= random.randint(0, 2)
    if board [rrow] [rcol] == '#':
        board [rrow] [rcol] = 'O'
    else:
        computer_ai_plays()
#user is asked where he wwants to play, if he tries to play where the oponent is it loops back.
def checkwinner():
    if (board [0][0]== board [0][1] == board [0][2] and board [0][0] != '#') or  (board [1][0] == board [1][1]== board [1][2] and board [1][2] != '#') or (board [2][0] == board [2][1] == board [2][2] and board [2][2] != '#'):
        print ('congrats someone won through rows')
        return 'stop'
    elif (board [0][0] == board [1][0] == board [2][0] and board [2][0] != '#') or (board [0][1] == board [1][1] == board [2][1] and board [0][1] != '#') or (board [0][2] == board [1][2] == board [2][2] and board [2][2] != '#'):
        print ('congrats someone won through column ')
        return 'stop'
    elif (board [0][0] == board [1][1] == board [2][2] and board [2][2] != '#') or (board [0][2] == board [1][1] == board [2][0] and board[2][0] != '#'):
        print ('congrats someone won through diagonal')
        return 'stop'
    hashes = 0
    for r in range (3):
        for c in range (3):
            if board [r] [c] == '#':
                hashes += 1
    if hashes == 0:
        print ('its a draw')
        return 'stop'

def userplays():
    try:
        row=int(input('which row do you want to put your thing in ' ))
        column= int(input('which column do you want to put your thing in '))
        if board [row] [column] == '#':
            board [row] [column] = 'X'
        else:
            print ('Cant play there, someone already played there you silly billy')
            userplays()
    except:
        print ('please input either 0, 1 or 2                     ')
        userplays()

for i in range(5):
    computer_ai_plays()
# display board and ask player to choose row and column where to play with O
    print('    0    1    2 ')
    for i in range(3):
        print (i, board[i])
    # user picks where to play

    if checkwinner() == 'stop':
        break

    quit=input('do you give up, type "yes" or press enter ')
    if quit == 'yes':
        break

    userplays()
    if checkwinner() == 'stop':
        break

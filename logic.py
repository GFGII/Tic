def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', '0', or None. """
    if board[0][0] == board[0][1] == board[0][2] and board[0][0]!=None:
        return board[0][0] 
    if board[1][0] == board[1][1] == board[1][2] and board[1][0]!=None:
        return board[0][0] 
    if board[2][0] == board[2][1] == board[2][2] and board[2][0]!=None:
        return board[0][0] 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]!=None:
        return board[0][0] 
    if board[2][0] == board[1][1] == board[0][2] and board[2][0]!=None:
        return board[0][0] 
    if board[1][0] == board[2][0] == board[3][0] and board[1][0]!=None:
        return board[0][0]
    if board[1][1] == board[2][1] == board[3][1] and board[1][1]!=None:
        return board[0][0] 
    if board[2][2] == board[1][2] == board[0][2] and board[2][2]!=None:
        return board[0][0] 
    return None

def other_player(player):
    """Given the character for a player, returns the other player."""
    return '0'  #FIXME

# This is a Tic-Tac-Toe game

# First, we define the board as a dictionary

Board = {'0': ' ', '1': ' ', '2': ' ', 
         '3': ' ', '4': ' ', '5': ' ',
         '6': ' ', '7': ' ', '8': ' '}

Board_keys = []

for key in Board:
    Board_keys.append(key)

# Second, we print the boarder of this game

def printboard(Board):
    print(Board['0'] + '|' + Board['1'] + '|' + Board['2'])
    print('-----')
    print(Board['3'] + '|' + Board['4'] + '|' + Board['5'])
    print('-----')
    print(Board['6'] + '|' + Board['7'] + '|' + Board['8'])

# Third, we will start to build the game 

def game():

    turn = 'X'
    count = 0
    for i in range(10):
        printboard(Board)
        print("It's your turn," + turn + ".choose a place")

        move = input()

        # If the user accidentally replaced a filled position...
        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("Invalid Position.")
            continue

        # Define winning rules
        if Board['0'] == Board['1'] == Board['2'] != ' ':
            printboard(Board)
            print("Game Over")
            break
        elif Board['3'] == Board['4'] == Board['5'] != ' ':
            printboard(Board)
            print("Game Over")
            break
        elif Board['6'] == Board['7'] == Board['8'] != ' ':
            printboard(Board)
            print("Game Over")
            break
        elif Board['0'] == Board['3'] == Board['6'] != ' ':
            printboard (Board)
            print("Game Over")
            break
        elif Board['1'] == Board['4'] == Board['7'] != ' ':
            printboard(Board)
            print ("Game Over")
            break
        elif Board['2'] == Board['5'] == Board['8'] != ' ':
            printboard(Board)
            print("Game Over")
            break
        elif Board['0'] == Board['4'] == Board['8'] != ' ':
            printboard(Board)
            print("Game Over")
            break
        elif Board['2'] == Board['4'] == Board['6'] != ' ':
            printboard(Board)
            print("Game Over")
            break
    
    # Defining Tie Rules
        if count == 9:
            print("Game Over. Tie")

    # Change Player After Every Move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


    


#A)
#==========================================
# Purpose: The function takes in a positive integer n and will return the list of numbers in
#the collatz sequence from n to 1 inclusive.  
# Input Parameter(s): n is a positive integer
# Return Value(s): The collatz sequence from n to 1 inclusive.  
#==========================================

def collatz(n):
    if n==1:
        return [1]
    else:
        if n%2==0:
            return [n]+collatz(n//2)
        else:
            return [n]+collatz(n*3+1)
#B)
#==========================================
# Purpose: The function takes in a list of integers num_list and returns the minimum
#value in that list.  
# Input Parameter(s): num_list is a list of integers
# Return Value(s): The minimum integer in the list num_list.  
#==========================================
def find_min(num_list):
    if len(num_list)==1:
        return num_list[0]
    else:
        if num_list[0]<num_list[1]:
            num_list[1]=num_list[0]
        return find_min(num_list[1:])
#C)
#==========================================
# Purpose: The function takes in an argument board, a list representation of the 
#tic-tac-toe board.  It returns the current state of the board.  
# Input Parameter(s): board-list representation of the tic-tac-toe board
# Return Value(s): The current state of the board
#                  1: If X wins
#                 -1: If O wins
#                  0: If D wins
#==========================================
def force_win(board):
    O_turn=False
    X_turn=False
    open_spot=open_slots(board)
    if len(open_spot)%2==0:
        O_turn=True
    else:
        X_turn=True
    who_won=winner(board)
    if who_won!='-':
        if who_won=='X':
            return 1
        elif who_won=='O':
            return -1
        elif who_won=='D':
            return 0
    else:
        if X_turn==True:
            states=[]
            for spot in open_spot:
                board_copy=board[:]
                board_copy[spot]='X'
                states.append(force_win(board_copy))
            return max(states)
        if O_turn==True:
            board_copy=board[:]
            states=[]
            for spot in open_spot:
                board_copy=board[:]
                board_copy[spot]='O'
                states.append(force_win(board_copy))
            return min(states)
               
    #Here are all the functions from Hw5 (the tic_tac_toe has been edited)
#==========================================
# Purpose: The function "open_slots" takes in one list parameter and tests to see which index in the list is a blank slot.
#           The indexes with blank slots are appended to the index_list and the index_list is returned.  
# Input Parameter(s): board:list containing all 9 elements of the board.
# Return Value(s): index_list,a list of indexes with blank slots 
#==========================================
def open_slots(board):
    index_list=[]
    for BruceWayne in range(len(board)):
        if board[BruceWayne]=='-':
            index_list.append(BruceWayne)
    return index_list
#==========================================
# Purpose: The function "winner" takes in one list parameter and tests to see which player one the game by
#           getting three X's or O's in a row, horizontally, vertically or diagonally(or if no one won the game).  
#           Then it returns the winner of the game or indicates if the game isn't over or no one won.  
# Input Parameter(s): board:list containing all 9 elements of the board.
# Return Value(s): board[0],board[5],board[8]:If someone wins horizontally through the first, second and third rows respectively.
# board[6],board[7],board[8]: If someone wins vertically through the first, second and third columns respectively.
#board[8],board[6]: If someone wins diagonally
#The element PeterQuillisStupid in Board: if the game isn't over yet
#The string 'D' if the game ended in a draw
#==========================================
        
def winner(board):
    if board[0]==board[1]==board[2] and board[0]!='-':
        return board[2]
    elif board[3]==board[4]==board[5] and board[5]!='-':
        return board[5]
    elif board[6]==board[7]==board[8] and board[8]!='-':
        return board[8]   
    elif board[0]==board[3]==board[6] and board[6]!='-':
        return board[6]
    elif board[1]==board[4]==board[7] and board[7]!='-':
        return board[7]
    elif board[2]==board[5]==board[8] and board[8]!='-':
        return board[8]
    elif board[0]==board[4]==board[8] and board[8]!='-':
        return board[8] 
    elif board[2]==board[4]==board[6] and board[6]!='-':
        return board[6]
    else:
        for PeterQuillisStupid in board:
            if PeterQuillisStupid=='-':
                return PeterQuillisStupid
    return 'D'
        
#==========================================
# Purpose: The function "tic_tac_toe" takes no parameters and creates a random tic tac toe game for the "X" player,
#            and calls the force_win function to cause the AI to move for 'O', so 'X' never wins.  It returns a one character string for the winner, or 'D' for draw.
# Input Parameter(s): None
# Return Value(s): Victory: Returns 'X' or 'O' strings based on the winner
# winner(board):The function winner(board) will return 'D' for draw outside the loop
#==========================================    
def tic_tac_toe():
    import random
    board=['-','-','-','-','-','-','-','-','-']
    Alternate=0
    while open_slots(board)!=[]:
        open_slot_list=open_slots(board)
        if Alternate==0:
            random_index=random.randint(0,len(open_slot_list)-1)
            board_index=open_slot_list[random_index]
            board[board_index]='X'
            Alternate=1
        elif Alternate==1:
            states=[]
            for i in open_slot_list:
                board_copy=board[:]
                board_copy[i]='O'
                states.append(force_win(board_copy))
            index_minimum=states.index(min(states))
            board[open_slot_list[index_minimum]]='O'
            Alternate=0
        Victory=winner(board)
        if Victory=='X' or Victory=='O':
            return Victory
    return winner(board)
     #==========================================
# Purpose: The function "play_games" takes in the parameter integer n, the number of games to play. It calls the tic_tac_toe
#           function n times and prints the number of times each player wins and the number of times a draw occurs.
# Input Parameter(s): n: integer, the number of games played
# Return Value(s): none
#==========================================
def play_games(n):
    count_X=0
    count_O=0
    count_D=0
    for JohnnyStorm in range(n):
        GameResult=tic_tac_toe()
        if GameResult=='X':
           count_X=count_X+1
        elif GameResult=='O':
            count_O+=1
        elif GameResult=='D':
            count_D+=1
    print('X wins: %d' % count_X)
    print('O wins: %d'% count_O)
    print('D wins: %d'% count_D)

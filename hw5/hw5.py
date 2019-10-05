#a)
#==========================================
# Purpose: The function "wizards" takes in three list
#           parameters and tests to see which of the names appears in all three lists.
#The names that appear in all three lists are appended to the wizards_list and the wizards_list is returned.  
# Input Parameter(s): grades:list of students who get good grades
#life:list of students who have a life
#sleep:List of students who get enough sleep
# Return Value(s): wizards_list, the list of wizards
#==========================================
def wizards(grades,life,sleep):
    wizards_list=[]
    for Hulk in grades:
        for Spidey in life:
            if Hulk==Spidey:
                for IronMan in sleep:
                    if IronMan==Spidey:
                        wizards_list.append(IronMan)
    return wizards_list
                    
#b)
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
    if board[0]==board[1]==board[2]:
        return board[0]
    if board[3]==board[4]==board[5]:
        return board[5]
    if board[6]==board[7]==board[8]:
        return board[8]   
    if board[0]==board[3]==board[6]:
        return board[6]
    if board[1]==board[4]==board[7]:
        return board[7]
    if board[2]==board[5]==board[8]:
        return board[8]
    if board[0]==board[4]==board[8]:
        return board[8] 
    if board[2]==board[4]==board[6]:
        return board[6]
    for PeterQuillisStupid in board:
        if PeterQuillisStupid=='-':
            return PeterQuillisStupid
    return 'D'
        
#==========================================
# Purpose: The function "tic_tac_toe" takes no parameters and creates a random tic tac toe game that the
#           computer plays against itself.  It returns a one character string for the winner, or 'D' for draw.
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
        random_index=random.randint(0,len(open_slot_list)-1)
        board_index=open_slot_list[random_index]
        if Alternate==0:
            board[board_index]='X'
            Alternate=1
        elif Alternate==1:
            board[board_index]='O'
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
          
        
       
        
                
        

# Homework 5 (hw5)

 - Grader Name: Alex Overman
 - Grader Email: ayres036@umn.edu
 - Homework Total: 40
 - Total Points Earned: 40



## Overall Deductions

#### Points Deducted:

-   Incorrect named/submitted source file, functions, or classes (20%)
-   Constraints not followed (40%)
-   Failure to execute due to syntax errors (30%)



## Problem 1 (10/10 pts)

#### Points Deducted:

**+4** correct logic/approach

-   -1 does not return a list of students that are wizards

-   -3 incorrect logic for iterating over lists

**+6** (1 pt each) 6 test cases



## Problem 2 (30/30 pts)

### 5/5 points : play_games(n)

#### Points Deducted:

**+3** correct logic/approach

-   -1 Does not call tic-tac-toe n times

-   -2 Incorrect print formatting / returns something

**+2** Code tested with n = 50, Win Rates should be around those below:

-   X winrate 56-60%

-   O winrate 27-31%

-   Draw 11-15%



### 10/10 points : winner(board)

#### Points Deducted:

**+5** correct logic/approach

-   -2 missing a case (a row/col/diagonal etc)

-   -2 doesn’t check for draws

-   -1 doesn’t return the correct winner/draw

**+5** (0.5 pts each) 10 test cases



### 5/5 points : open_slots(board)

#### Points Deducted:

**+2** correct logic

-   Example: loops over board and stores empty index to new list

**+3** (1 pt each) 3 test cases

  

### 09/10 points : tic-tac-toe()

#### Points Deducted:

**+4** Correct loop structure

-   -1 X is not first

-   -1 turns are not alternated

-   -1 always only plays 9 turns

**+2** The current player must choose an empty space on their turn

-   -1 if they don’t call open_slots to check for an empty spaces

**+2** Game ends when someone wins/all spaces filled

-   -1 does not call winner() to check for wins

**+2** Returns correct winner or draw


## Additional Comments

**Great work here!  Your variable names made me smile and I thank you for it, but in the future another TA might dock points for variable names that aren't descriptive of their purpose. Otherwise, you have great solutions here, and your templates are very thorough.**

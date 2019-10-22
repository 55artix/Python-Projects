### Early Feedback for Homework 7 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Monday and Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Run on October 22, 00:48:20 AM.

+ Pass: Change into directory "hw7".

+ Pass: Check that file "hw7.py" exists.

+ Pass: Secret Test

+ Fail: Check that a Python file "hw7.py" has no syntax errors.

    Python file hw7.py does not terminate within 1 seconds.

    Check for infinite loops/recursion.



+ Skip: 
Check that the result of evaluating
   ```
   collatz(42)
   ```
   matches the pattern `[42, 21, 64, 32, 16, 8, 4, 2, 1]`.

   


  This test was not run because of an earlier failing test.

+ Skip: 
Check that the result of evaluating
   ```
   find_min([4, 0, -6, 5, -8, 6, -5, -6])
   ```
   matches the pattern `-8`.

   


  This test was not run because of an earlier failing test.

+ Skip: 
Check that the result of evaluating
   ```
   force_win(['-', '-', 'X', '-', 'O', 'O', 'X', 'O', 'X'])
   ```
   matches the pattern `-1`.

   


  This test was not run because of an earlier failing test.

+ Skip: 
Check that the result of evaluating
   ```
   tic_tac_toe() in ['O', 'D']
   ```
   matches the pattern `True`.

   


  This test was not run because of an earlier failing test.

+ Skip: 
Check that the result of evaluating
   ```
   ([tic_tac_toe() for i in range(20)]).count('X')
   ```
   matches the pattern `0`.

   


  This test was not run because of an earlier failing test.

+ Skip: 
Check that the result of evaluating
   ```
   1 < ([tic_tac_toe() for i in range(60)]).count('D') < 30
   ```
   matches the pattern `True`.

   


  This test was not run because of an earlier failing test.


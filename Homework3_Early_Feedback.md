### Early Feedback for Homework 3 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Disclaimer on this week's test in particular: the testing script is not particularly good at handling user input problems.

You might get some very strange feedback on parts B or C if you call input the wrong number of total times or cause errors.

Run on September 25, 00:04:32 AM.

+ Pass: Change into directory "hw3".

+ Pass: Check that file "hw3.py" exists.

+ Pass: Check that Python file "hw3.py" only imports permitted modules.

+ Pass: Check that a Python file "hw3.py" has no syntax errors.

    Python file "hw3.py" has no syntax errors.



+ Fail: 
Check that the result of evaluating
   ```
   sound(30)+sound(31)
   ```
   matches the pattern `'RuffBark'`.

   


   Test failed. The following errors were reported:

```
 
Ruff
Bark
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

```


+ Fail: 
Check that the result of evaluating
   ```
   'Result: '+choice('Its 3 AM','Sleep','Write','Party')
   ```
   with user input sequence
   ```
   'Non-numeric input', '1.5', '1'
   ```
   matches the pattern `'Result: 1'`.

   


   Test failed. The following errors were reported:

```
 
Its 3 AM

1.Sleep
2 Write
3 Party
Choose 1, 2, or 3:Non-numeric input
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw3.py", line 40, in choice
    Your_Choice = int(input('Choose 1, 2, or 3:'))
ValueError: invalid literal for int() with base 10: 'Non-numeric input'

```


+ Fail: 
Check that the result of evaluating
   ```
   adventure()
   ```
   with user input sequence
   ```
   '2', '3', 'Bees?', '4', '1'
   ```
   matches the pattern `True`.

   


   Test failed. The following errors were reported:

```
 
Choose Your Poison

1.Arsenic
2 Alcohol
3 Anti-freeze
Choose 1, 2, or 3:2
2
Choose someone to save you

1.Captain America
2 Iron Man
3 Wonder Woman
Choose 1, 2, or 3:3
3
You have woken up from your coma to discover that you have superpowers!  Choose a team to join:

1.The Avengers
2 The Justice League
3 The X-Men
Choose 1, 2, or 3:Bees?
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw3.py", line 84, in adventure
    the_choice = choice("You have woken up from your coma to discover that you have superpowers!  Choose a team to join:", "The Avengers","The Justice League","The X-Men")
  File "hw3.py", line 40, in choice
    Your_Choice = int(input('Choose 1, 2, or 3:'))
ValueError: invalid literal for int() with base 10: 'Bees?'

```


+ Pass: 
Check that the result of evaluating
   ```
   adventure()
   ```
   with user input sequence
   ```
   '2', '2', '2', '2'
   ```
   matches the pattern `False`.

   





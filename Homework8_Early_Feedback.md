### Early Feedback for Homework 8 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Monday and Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Run on October 30, 01:55:27 AM.

+ Pass: Change into directory "hw8".

+ Pass: Check that file "hw8.py" exists.

+ Pass: Secret Test

+ Pass: Check that a Python file "hw8.py" has no syntax errors.

    Python file "hw8.py" has no syntax errors.



+ Pass: Writing test8.csv into local directory  
File Contents:
```
hw8 Grade but not really,hw8 Grade,Full Name,Destined for Greatness
0,????,Fake Name,Yes
0,????,Not Real,Yes
0,????,Wait For It,Yes
0,????,Christina Lu,Yes

```




+ Pass: 
Check that the result of evaluating
   ```
   get_data_list('grades6.csv')
   ```
   matches the pattern `-1`.

   




+ Pass: 
Check that the result of evaluating
   ```
   get_data_list('test8.csv')[:-1]
   ```
   matches the pattern `['hw8 Grade but not really,hw8 Grade,Full Name,Destined for Greatness\n','0,????,Fake Name,Yes\n','0,????,Not Real,Yes\n','0,????,Wait For It,Yes\n']`.

   




+ Pass: 
Check that the result of evaluating
   ```
   hw8_index('hw8 Grade but not really,hw8 Grade,Full Name,Destined for Greatness\n')
   ```
   matches the pattern `1`.

   




+ Pass: 
Check that the result of evaluating
   ```
   hw8_index('Even though,one of the entries,contains it,hw8 Grade is not,an entry here\n')
   ```
   matches the pattern `-1`.

   




+ Pass: 
Check that the result of evaluating
   ```
   alter_grade('0,????,Fake Name,Yes\n',1)
   ```
   matches the pattern `'0,40,Fake Name,Yes\n'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   alter_grade('overwriting 40,with 40,should,do,nothing,40,\n',5)
   ```
   matches the pattern `'overwriting 40,with 40,should,do,nothing,40,\n'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   haxx('grades6.csv')
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   haxx('test8.csv')
   ```
   matches the pattern `True`.

   




+ Pass: Checking that contents of test8.csv
```
hw8 Grade but not really,hw8 Grade,Full Name,Destined for Greatness
0,????,Fake Name,Yes
0,????,Not Real,Yes
0,????,Wait For It,Yes
0,40,Christina Lu,Yes

```
match the pattern:
```
hw8 Grade but not really,hw8 Grade,Full Name,Destined for Greatness
0,????,Fake Name,Yes
0,????,Not Real,Yes
0,????,Wait For It,Yes
0,40,Christina Lu,Yes

```





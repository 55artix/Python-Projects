### Early Feedback for Homework 9 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Monday and Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Run on November 05, 01:47:37 AM.

+ Pass: Change into directory "hw9".

+ Pass: Check that file "hw9.py" exists.

+ Pass: Secret Test

+ Pass: Check that a Python file "hw9.py" has no syntax errors.

    Python file "hw9.py" has no syntax errors.



+ Pass: Writing darth_plagueis.txt into local directory  
File Contents:
```
Did you ever hear the Tragedy of Darth Plagueis the wise .
I thought not .
It's not a story the Jedi would tell you .
It's a Sith legend .
Darth Plagueis was a Dark Lord of the Sith so powerful and so wise he could use the Force to influence the midichlorians to create life .
He had such a knowledge of the dark side that he could even keep the ones he cared about from dying .
The dark side of the Force is a pathway to many abilities some consider to be unnatural .
He became so powerful the only thing he was afraid of was losing his power which eventually of course he did .
Unfortunately he taught his apprentice everything he knew then his apprentice killed him in his sleep .
Ironic .
He could save others from death but not himself .

```




+ Pass: 
Check that the result of evaluating
   ```
   first_words('darth_plagueis.txt')
   ```
   matches the pattern `['Did', 'I', "It's", "It's", 'Darth', 'He', 'The', 'He', 'Unfortunately', 'Ironic', 'He']`.

   




+ Fail: 
Check that the result of evaluating
   ```
   next_words('darth_plagueis.txt')
   ```
   matches the pattern `{'Did': ['you'], 'you': ['ever', '.'], 'ever': ['hear'], 'hear': ['the'], 'the': ['Tragedy', 'wise', 'Jedi', 'Sith', 'Force', 'midichlorians', 'dark', 'ones', 'Force', 'only'], 'Tragedy': ['of'], 'of': ['Darth', 'the', 'the', 'the', 'was', 'course'], 'Darth': ['Plagueis', 'Plagueis'], 'Plagueis': ['the', 'was'], 'wise': ['.', 'he'], 'I': ['thought'], 'thought': ['not'], 'not': ['.', 'a', 'himself'], "It's": ['not', 'a'], 'a': ['story', 'Sith', 'Dark', 'knowledge', 'pathway'], 'story': ['the'], 'Jedi': ['would'], 'would': ['tell'], 'tell': ['you'], 'Sith': ['legend', 'so'], 'legend': ['.'], 'was': ['a', 'afraid', 'losing'], 'Dark': ['Lord'], 'Lord': ['of'], 'so': ['powerful', 'wise', 'powerful'], 'powerful': ['and', 'the'], 'and': ['so'], 'he': ['could', 'could', 'cared', 'was', 'did', 'taught', 'knew'], 'could': ['use', 'even', 'save'], 'use': ['the'], 'Force': ['to', 'is'], 'to': ['influence', 'create', 'many', 'be'], 'influence': ['the'], 'midichlorians': ['to'], 'create': ['life'], 'life': ['.'], 'He': ['had', 'became', 'could'], 'had': ['such'], 'such': ['a'], 'knowledge': ['of'], 'dark': ['side', 'side'], 'side': ['that', 'of'], 'that': ['he'], 'even': ['keep'], 'keep': ['the'], 'ones': ['he'], 'cared': ['about'], 'about': ['from'], 'from': ['dying', 'death'], 'dying': ['.'], 'The': ['dark'], 'is': ['a'], 'pathway': ['to'], 'many': ['abilities'], 'abilities': ['some'], 'some': ['consider'], 'consider': ['to'], 'be': ['unnatural'], 'unnatural': ['.'], 'became': ['so'], 'only': ['thing'], 'thing': ['he'], 'afraid': ['of'], 'losing': ['his'], 'his': ['power', 'apprentice', 'apprentice', 'sleep'], 'power': ['which'], 'which': ['eventually'], 'eventually': ['of'], 'course': ['he'], 'did': ['.'], 'Unfortunately': ['he'], 'taught': ['his'], 'apprentice': ['everything', 'killed'], 'everything': ['he'], 'knew': ['then'], 'then': ['his'], 'killed': ['him'], 'him': ['in'], 'in': ['his'], 'sleep': ['.'], 'Ironic': ['.'], 'save': ['others'], 'others': ['from'], 'death': ['but'], 'but': ['not'], 'himself': ['.']}`.

   


   Your solution evaluated incorrectly and produced:

 
```
 
{'Did': ['you'], 'you': ['ever', '.'], 'ever': ['hear'], 'hear': ['the'], 'the': ['Tragedy', 'wise', 'Jedi', 'Sith', 'Force', 'midichlorians', 'dark', 'ones', 'Force', 'only'], 'Tragedy': ['of'], 'of': ['Darth', 'the', 'the', 'the', 'was', 'course'], 'Darth': ['Plagueis', 'Plagueis'], 'Plagueis': ['the', 'was'], 'wise': ['.', 'he'], 'I': ['thought'], 'thought': ['not'], 'not': ['.', 'a', 'himself'], "It's": ['not', 'a'], 'a': ['story', 'Sith', 'Dark', 'knowledge', 'pathway'], 'story': ['the'], 'Jedi': ['would'], 'would': ['tell'], 'tell': ['you'], 'Sith': ['legend', 'so'], 'legend': ['.'], 'was': ['a', 'afraid', 'losing'], 'Dark': ['Lord'], 'Lord': ['of'], 'so': ['powerful', 'wise', 'powerful'], 'powerful': ['and', 'the'], 'and': ['so'], 'he': ['could', 'could', 'cared', 'was', 'did', 'taught', 'knew'], 'could': ['use', 'even', 'save'], 'use': ['the'], 'Force': ['to', 'is'], 'to': ['influence', 'create', 'many', 'be'], 'influence': ['the'], 'midichlorians': ['to'], 'create': ['life'], 'life': ['.'], 'He': ['had', 'became', 'could'], 'had': ['such'], 'such': ['a'], 'knowledge': ['of'], 'dark': ['side', 'side'], 'side': ['that', 'of'], 'that': ['he'], 'even': ['keep'], 'keep': ['the'], 'ones': ['he'], 'cared': ['about'], 'about': ['from'], 'from': ['dying', 'death'], 'dying': ['.'], 'The': ['dark'], 'is': ['a'], 'pathway': ['to'], 'many': ['abilities'], 'abilities': ['some'], 'some': ['consider'], 'consider': ['to'], 'be': ['unnatural'], 'unnatural': ['.'], 'became': ['so'], 'only': ['thing'], 'thing': ['he'], 'afraid': ['of'], 'losing': ['his'], 'his': ['power', 'apprentice', 'apprentice', 'sleep'], 'power': ['which'], 'which': ['eventually'], 'eventually': ['of'], 'course': ['he'], 'did': ['.'], 'Unfortunately': ['he'], 'taught': ['his'], 'apprentice': ['everything', 'killed'], 'everything': ['he'], 'knew': ['then'], 'then': ['his'], 'killed': ['him'], 'him': ['in'], 'in': ['his'], 'sleep': ['.'], 'Ironic': ['.'], 'save': ['others'], 'others': ['from'], 'death': ['but'], 'but': ['not'], 'himself': ['.'], '': []}
```



+ Pass: 
Check that the result of evaluating
   ```
   fanfic('darth_plagueis.txt')
   ```
   could be produced from the source file.

   


   Your solution produced: 
```
 
He had such a knowledge of the Force is a knowledge of the Jedi would tell you ever hear the Jedi would tell you ever hear the only thing he taught his sleep .
I thought not himself .
I thought not .
The dark side that he could even keep the Sith so powerful and so wise he could even keep the Jedi would tell you .
Unfortunately he did .
Unfortunately he taught his apprentice killed him in his power which eventually of was a Sith so powerful and so powerful and so powerful and so wise .
It's a Dark Lord of course he taught his power which eventually of the only thing he cared about from dying .
Did you ever hear the ones he could use the only thing he could save others from dying .
Unfortunately he could use the dark side that he could use the Force is a story the Sith so wise he knew then his sleep .
He had such a story the Sith so powerful the Tragedy of the Force is a knowledge of was losing his apprentice killed him in his power which eventually of the midichlorians to influence the Sith so powerful and so wise he was losing his power which eventually of Darth Plagueis the Force to influence the wise .
```




+ Fail: 
Check that the result of evaluating
   ```
   total_txt_size({'z':{'y':{'x.txt':6, 'w.txt.zip.py':2, 'vu':{}, 'tea.txt':4}, 's.c':3, 'rq':{'p':{}, 'o':{'nml.txt':1}}}, 'kjih.java':5})
   ```
   matches the pattern `11`.

   


   Your solution evaluated incorrectly and produced:

 ` 
21`



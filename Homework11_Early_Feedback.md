### Early Feedback for Homework 11 (THIS IS NOT YOUR GRADE, the assignment isn't due yet)

These tests are run on Monday and Tuesday nights around 11:55 PM, so if you didn't submit before then you can ignore this document

Passing these tests is not a guarantee of a perfect homework score: the tests do not check everything that the TAs will.

Any questions/errors with the Automated Feedback should be reported to Nathan Taylor: taylo740@umn.edu

Run on November 19, 01:46:41 AM.

+ Pass: Change into directory "hw11".

+ Pass: Check that file "hw11.py" exists.

+ Pass: Secret Test

+ Pass: Check that a Python file "hw11.py" has no syntax errors.

    Python file "hw11.py" has no syntax errors.



+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).name
   ```
   matches the pattern `'Dora'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).level
   ```
   matches the pattern `5`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).strength
   ```
   matches the pattern `3`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).speed
   ```
   matches the pattern `4`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).power
   ```
   matches the pattern `2`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).HP
   ```
   matches the pattern `30`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Adventurer('Dora',5,3,4,2).hidden
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   repr(Adventurer('Dora',5,3,4,2))
   ```
   matches the pattern `'Dora - HP: 30'`.

   




+ Pass: 
Check that the result of evaluating
   ```
   kenobi = Adventurer('Obi-Wan',13,3,5,7); skywalker = Adventurer('Anakin',12,6,6,4); skywalker.attack(kenobi); kenobi.HP
   ```
   matches the pattern `68`.

   




+ Pass: 
Check that the result of evaluating
   ```
   kenobi = Adventurer('Obi-Wan',13,3,5,7); skywalker = Adventurer('Anakin',12,6,6,4); skywalker.attack(kenobi); skywalker.attack(kenobi); kenobi.HP
   ```
   matches the pattern `58`.

   




+ Pass: 
Check that the result of evaluating
   ```
   tiger = Adventurer('Tony',5,2,4,1); cena = Adventurer('John',8,6,5,2); cena.hidden = True; tiger.attack(cena); cena.HP
   ```
   matches the pattern `48`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).level
   ```
   matches the pattern `16`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).strength
   ```
   matches the pattern `20`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).speed
   ```
   matches the pattern `14`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).power
   ```
   matches the pattern `16`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).HP
   ```
   matches the pattern `192`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Fighter('Roy',16,20,14,16).hidden
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   isinstance(Fighter('Roy',16,20,14,16), Adventurer)
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Thief('Haley',16,12,22,14).HP
   ```
   matches the pattern `128`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Thief('Haley',16,12,22,14).hidden
   ```
   matches the pattern `True`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Wizard('Vaarsuvius',16,8,12,20).HP
   ```
   matches the pattern `96`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Wizard('Vaarsuvius',16,8,12,20).hidden
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   Wizard('Vaarsuvius',16,8,12,20).fireballs_left
   ```
   matches the pattern `20`.

   




+ Pass: 
Check that the result of evaluating
   ```
   b2 = Fighter('2B',5,8,5,2); s9 = Thief('9S',3,2,6,4); b2.attack(s9); s9.HP
   ```
   matches the pattern `24`.

   




+ Pass: 
Check that the result of evaluating
   ```
   b2 = Fighter('2B',5,8,5,2); s9 = Thief('9S',3,2,6,4); b2.attack(s9); s9.hidden
   ```
   matches the pattern `True`.

   




+ Fail: 
Check that the result of evaluating
   ```
   b2 = Fighter('2B',5,8,5,2); s9 = Thief('9S',3,2,6,4); s9.attack(b2); b2.HP
   ```
   matches the pattern `15`.

   


   Test failed. The following errors were reported:

```
 
9S sneak attacks 2B for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Fail: 
Check that the result of evaluating
   ```
   b2 = Fighter('2B',5,8,5,2); s9 = Thief('9S',3,2,6,4); s9.attack(b2); b2.attack(s9); s9.HP
   ```
   matches the pattern `2`.

   


   Test failed. The following errors were reported:

```
 
9S sneak attacks 2B for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); a2.attack(s9); s9.HP
   ```
   matches the pattern `6`.

   




+ Fail: 
Check that the result of evaluating
   ```
   s9 = Thief('9S',3,2,6,4); s9.attack(s9); s9.HP
   ```
   matches the pattern `-21`.

   


   Test failed. The following errors were reported:

```
 
9S sneak attacks 9S for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); a2.attack(s9); a2.attack(s9); s9.HP
   ```
   matches the pattern `-2`.

   




+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); a2.attack(s9); a2.attack(s9); a2.fireballs_left
   ```
   matches the pattern `0`.

   




+ Fail: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); s9.attack(a2); a2.HP
   ```
   matches the pattern `-9`.

   


   Test failed. The following errors were reported:

```
 
9S sneak attacks A2 for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); a2.attack(s9); s9.attack(a2); a2.HP
   ```
   matches the pattern `30`.

   




+ Pass: 
Check that the result of evaluating
   ```
   koed = Adventurer('zzz',1,2,3,4); koed.HP = -99; duel(koed,koed)
   ```
   matches the pattern `False`.

   




+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); duel(a2,s9)
   ```
   matches the pattern `True`.

   




+ Fail: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); duel(s9,a2)
   ```
   matches the pattern `True`.

   


   Test failed. The following errors were reported:

```
 
9S - HP: 24
A2 - HP: 36
9S sneak attacks A2 for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 174, in duel
    adv1.attack(adv2)
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Fail: 
Check that the result of evaluating
   ```
   b2 = Fighter('2B',5,8,5,2); s9 = Thief('9S',3,2,6,4); duel(s9,b2)
   ```
   matches the pattern `False`.

   


   Test failed. The following errors were reported:

```
 
9S - HP: 24
2B - HP: 60
9S sneak attacks 2B for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 174, in duel
    adv1.attack(adv2)
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Pass: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); b2 = Fighter('2B',5,8,5,2); duel(a2,b2)
   ```
   matches the pattern `False`.

   




+ Fail: 
Check that the result of evaluating
   ```
   a2 = Wizard('A2',6,4,3,1); s9 = Thief('9S',3,2,6,4); b2 = Fighter('2B',5,8,5,2); duel(a2,b2); duel(s9,b2)
   ```
   matches the pattern `True`.

   


   Test failed. The following errors were reported:

```
 
A2 - HP: 36
2B - HP: 60
A2 casts fireball on 2B for 18 damage
2B attacks A2 for 22 damage
A2 - HP: 14
2B - HP: 42
A2 attacks 2B for 8 damage
2B attacks A2 for 22 damage
A2 - HP: -8
2B - HP: 34
2B wins!
False
9S - HP: 24
2B - HP: 34
9S sneak attacks 2B for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 174, in duel
    adv1.attack(adv2)
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Fail: 
Check that the result of evaluating
   ```
   tournament([Wizard('A2',6,4,3,1), Fighter('2B',5,8,5,2), Thief('9S',3,2,6,4)]).name
   ```
   matches the pattern `'9S'`.

   


   Test failed. The following errors were reported:

```
 
A2 - HP: 36
2B - HP: 60
A2 casts fireball on 2B for 18 damage
2B attacks A2 for 22 damage
A2 - HP: 14
2B - HP: 42
A2 attacks 2B for 8 damage
2B attacks A2 for 22 damage
A2 - HP: -8
2B - HP: 34
2B wins!
9S - HP: 24
2B - HP: 34
9S sneak attacks 2B for 45
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 215, in tournament
    return tournament(adv_list)
  File "hw11.py", line 198, in tournament
    duel_result=duel(player1,player2)
  File "hw11.py", line 174, in duel
    adv1.attack(adv2)
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```


+ Fail: 
Check that the result of evaluating
   ```
   tournament([Adventurer('Obi-Wan',13,3,5,7), Adventurer('Anakin',12,6,6,4), Adventurer('Tony',5,2,4,1), Adventurer('John',8,6,5,2), Wizard('Vaarsuvius',16,8,12,20), Fighter('Roy',16,20,14,16), Thief('Haley',16,12,22,14) ]).name
   ```
   matches the pattern `'Vaarsuvius'`.

   


   Test failed. The following errors were reported:

```
 
Haley - HP: 128
Roy - HP: 192
Haley sneak attacks Roy for 190
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "hw11.py", line 198, in tournament
    duel_result=duel(player1,player2)
  File "hw11.py", line 174, in duel
    adv1.attack(adv2)
  File "hw11.py", line 121, in attack
    print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage))+' damage'
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```



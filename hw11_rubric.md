# HW11 - CSCI1133 Rubric

 * Grader Name: **Dylan Tatham**
 * Grader email: **tatha005@umn.edu**
 * Homework Total: **40**
 * Grade: **40**

## General Deductions

* Incorrectly named/submitted source file, functions, or classes (20% per problem) 
* Constraints not followed (40% per problem) 
* Failure to execute due to syntax errors (30% per problem)
* Bad Style/Missing function templates (10% per problem)
* Redefines __ repr __ (-2 total)

## RPG Fight! (30 pts) :

### Adventurer (5 pts)

### Points Deducted : 0

* +2 __ init __ (deduct 0.5 for each incorrect variable until at 0)
  * self.name
  * self.level
  * self.strength
  * self.speed
  * self.power
  * self.HP
  * self.hidden
* +1 __ repr __
  * +1 Correct formatting
* +2 attack(self, target)
  * +0.5 Checks for hidden target
  * +0.5 Correctly calculates attack damage
  * +0.5 Deducts target health
  * +0.5 Correct output messages

### Fighter (5 pts)

### Points Deducted : 0

* +3 __ init __
  * +1 Correctly calls Adventurer class
  * +1 Does not redefine any member variables 
  * +1 redefines self.HP
* +2 attack(self, target)
  * +0.5 Checks for hidden target
  * +0.5 Correctly calculates attack damage
  * +0.5 Deducts target health
  * +0.5 Correct output messages

### Thief  (7 pts)

### Points Deducted : 0
* +2 __ init __
  * +0.5 Correctly calls Adventurer class
  * +0.5 Does not redefine any member variables
  * +0.5 self.hidden
  * +0.5 self.HP
* +5 __ attack __
  * +1 correctly calls Adventurer class for standard attack
  * +0.5 correctly decrements target health
  * +0.5 correctly formats output statements
  * +0.5 correctly computes damage for sneak attack
  * +2.5 (0.5 pts each) correct sneak attack logic
    * Target hidden, Thief not hidden -> does not attack
    * Target not hidden, Thief hidden -> sneak attack
    * Target hidden + speed higher, Thief hidden -> does not attack
    * Target hidden, Thief hidden + speed higher -> sneak attack
    * Target hidden, Thief hidden, speed equal -> sneak attack

### Wizard (6 pts)

### Points Deducted : 0

* +2 __ init __
  * +0.5 Correctly calls Adventurer class
  * +0.5 Does not redefine any member variables
  * +1 self.fireballs_left = power
* +4 attack(self, target)
  * +1 correctly calls Adventurer class for standard attack
  * +0.5 correctly checks fireballs_left
  * +0.5 correctly decrements fireballs_left
  * +0.5 correctly decrements target's health
  * +0.5 correctly changes target's hidden status
  * +0.5 correctly formats output statements
  * +0.5 correctly calculate damage

### Duel (7 pts)

### Points Deducted : 0

* +1 correct function name/parameters/return type
* +1 correct while loop or recursive approach to running the duel
* +1 correctly formats output statements
* +0.5 returns False if player 1 or both players cannot duel before the match starts (prior to modifying health totals)
* +0.5 returns True if player 2 can't duel before the match starts (prior to modifying health totals)
* +0.5 player 1 always goes first
* +2.5 checks player conditions after every attack
  * +1 correctly returns player 1 win 
  * +1 correctly returns player 2 win
  * +0.5 correctly returns loss for both players

## The Ultimate Showdown (10 pts) : 

+ +1 correct function name/parameters
+ +1 correctly returns winner
+ +1 while loop or recursive approach to running the duel
+ +2 correctly sorts lists on adventurer health
+ +2 uses two healthiest players for duel
+ +1 weaker player goes first in duel
+ +2 correctly removes loser from list

## Grader Comments 
Great job!

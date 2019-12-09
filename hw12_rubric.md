# 1133 HW12 Rubric

 * Grader Name: **Dylan Tatham**
 * Grader email: **tatha005@umn.edu**
 * Homework Total: **60**
 * Grade: **70**

## General Deductions

* Incorrectly named/submitted source file, functions, or classes (20% per problem) 
* Constraints not followed (40% per problem) 
  * Does not use the input() function anywhere in your code. It will break our grading scripts and result in major point penalties.
  * Must actually use the Pokemon class that's created by instantiating it and accessing it as some point in the code (i.e., don’t just create the class but then do the whole assignment without using it) 
* Failure to execute due to syntax errors (30% per problem)
* Bad Style (10% per problem)
* Updates incorrect labels/incorrect label layout (-2 entire HW)

## Pokemon Class (8 pts)

#### Points deducted : 

* +2 pt : Has instance variables for species name, dex number, catch rate, and speed 
* +2 pt : Has an overloaded __str__ method that returns the species name 
* +4 pts : Uses Pokemon class in SafariSimulator

## Safari Simulator (52 pts)

### __ init __ (6 pts)

#### Points deducted : 

* +3 Read in the information from pokedex.csv, and store it in some collection (list, dictionary, set, etc) of Pokemon objects. 
  * -1 Does not close file
  * -1 Does not store the data in some data structure **here**
  * 
* +1 Have some way of keeping track of the number of Safari balls left 
* +1 Have some way of keeping track of the caught Pokemon 
* +1 Call the nextPokemon method (after createWidgets) to start the first Pokemon encounter 



### createWidgets  (10 pts)

#### Points deducted :

* +2 Create/pack a Button for throwing a Safari Ball
* +2 Create/pack a Label for the Pokemon sprite image
* +2 Create/pack a Label for the Catch Probability
* +2 Bind throwBall to correct button
* +2 Sprite image shows up



### nextPokemon (14 pts)

####  Points deducted : 

* +2 Correctly choses a random Pokemon out of the 151 possibilities from their data structure
  * -1 Does not access data structure
  * -1 Does not randomly select
* Update the message label to “You encounter a wild [species name]” 
* +2 Update the catch probability label to the correct percentage
  * -1 Incorrect math
  * -1 Improper label update
* +2 Update the image label to use the given PhotoImage object 
* +2 Update the description to display the correct Pokemon
* +6 Make a PhotoImage object for the sprite of the current Pokemon, and save it to some instance variable
  * -3 Does not save image to instance variable
  * -3 Does not grab image correctly (ie. incorrect file path, does not use file= in function call)



### throwBall  (14 pts)

#### Points deducted :

* +1 Generate a random number between 0 and 1 using random.random() 
* +2 Use that number to determine whether the Pokemon was caught
* +2 Update the throwButton text to reflect the fact that one Safari ball was used 
  * -1 Does not decrement safari ball count
  * -1 Output message is incorrect
* +1 Change the message label to “Aargh! It escaped” if the Pokemon was not caught 
  * -1 Output message is incorrect
* +2 Stores captured Pokemon in data structure
* +2 Call endAdventure if this was the last Safari Ball 
* +2 Call nextPokemon if the Pokemon was caught 
* +2 SafariSimulator end



### Adventure (8 pts)

#### Points deducted :

* +1 Display “You’re out of balls, I hope you had fun!” in one of the labels 
* +1 Display "Oops, you caught 0 pokemon."
* +3 Display the number of Pokémon caught, and the list of their names, in another label
  * -1 Access data structure of caught Pokemon to check how many Pokemon have been caught
  * -1 Does not display number of Pokemon caught
  * -1 Does not display names of Pokemon caught
* +2 Remove all other buttons and labels so that the user can’t keep playing
* +1 Packs labels



## Grader Comments
Great job!

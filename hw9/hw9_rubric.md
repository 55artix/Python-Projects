# HW9 - CSCI1133 Rubric

 * Grader Name: **Sam Jirovec**
 * Grader email: **jirov004@umn.edu**
 * Homework Total: **40**
 * Grade: **38**

## General Deductions

* Incorrectly named/submitted source file (-8)
* Constraints not followed (-40% PER PROBLEM)
* Failure to execute due to syntax errors (-30% PER PROBLEM)

## first_words(5 pts):

* +1 Correct
  * Function definitions
  * Parameters
  * Return Type
* +1 Correctly opens/closes file (for reading)
* +2 Correctly grabs first word in each line
* +1 Test case

## next_words(8 pts): -2 (Test cases failed)

* +1 Correct
  * Function definitions
  * Parameters
  * Return Type
* +1 Correctly opens/closes file (for reading)
* +2 Correctly handles duplicates by adding onto the values and not resetting the key
  * -1 for incorrect logic
  * -1 for failed test case
* +2 Correctly places a period for a value if at the end of a sentence
  * -1 for incorrect logic
  * -1 for failed test case
* +1 Duplicate values exist 
  * -1/2 for incorrect logic
  * -1/2 for failed test case
* +1 Goes through all lines of the file
  * -1/2 for incorrect logic
  * -1/2 for failed test case

## fanfic(7 pts):

* +1 Correct
  * Function definitions
  * Parameters
  * Return Type
* +1 calling first_words and next_words to initialize lists
* +1 choosing 1st word randomly from first_words list
* +2 randomly selects from next_words list
* +1 looping until a period is reached
* +1 creates 10 sentences

## traverse(20 pts): 

### Logic

* +2 Correct
  * Function definitions
  * Parameters
  * Return Type
* +2 iterate through all keys
* +2 check for type(dict) properly
* +2 check for type(int) properly
* +2 check for .txt file correctly
* +2 correctly keep track of total memory take  up by text files
* +2 correctly adds up memory
* +4 correctly goes deeper into the dictionary (recursion recommended)

### Test Cases

* +1 correctly handles empty dictionaries
* +0.5 correctly handles a simple dictionary of files
* +0.5 correctly handles a complex dictionary of files that contains many different file types and also files with txt in the name and extension

## Grader Comments:  
Next_words should not be including the empty string as a key. 

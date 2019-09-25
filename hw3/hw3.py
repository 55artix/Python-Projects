
#hw3a)
#==========================================
# Purpose: The function prints out the sound that a dog makes based on the weight
# of the dog entered as an integer in the function.  
# Input Parameter(s): The dog's weight in pounds
# Return Value(s): No returns
#==========================================

def sound(weight):
    if weight<13:
        return 'Yip'
    elif weight>=13 and weight<=30:
        return 'Ruff'
    elif weight>=31 and weight<=70:
        return 'Bark'
    elif weight>70:
        return 'Boof'
    
#hw3b)
#==========================================
# Purpose: The function takes in four parameters. A prompt for a choice (text)
# and three options within the game.  If a valid option (1,2, or 3) is chosen,
# the value is returned.  If not, the choice is invalid, and the loop prompts
# you back to choose again.  
# Input Parameter(s):
# text - the prompt for the choices
# option1 - the first option in the game
# option2 - the second option in the game
# option3 - the third option in the game
# Return Value(s): The option that you've chosen.
#==========================================

def choice(text, option1, option2, option3):
    print(text)
    print()
    print('1.%s' % (option1))
    print('2 %s' % (option2))
    print('3 %s' % (option3))
    Your_choice=0
    while Your_choice==0:
        Your_input = input('Choose 1, 2, or 3:')
        if Your_input=='1' or Your_input=='2' or Your_input=='3':
            Your_choice=int(Your_input)
        else:
            print('invalid option\n')
    return Your_choice

#hw3c)
#==========================================
# Purpose: The adventure() function gives the player a series of choices leading to a series of multiple endings.    
# Input Parameter(s):
# none
# Return Value(s): Boolean values of true or false depending on the ending.  
#==========================================

def adventure():
    state = 1
    if  state == 1:
        the_choice = choice("Choose Your Poison","Arsenic","Alcohol","Anti-freeze")
        if the_choice == 1:
            print("You have died")
            return False
        elif the_choice == 2:
            state = 2
        elif the_choice == 3:
            state = 3
    if state == 2:
        the_choice = choice("Choose someone to save you", "Captain America", "Iron Man", "Wonder Woman")
        if the_choice == 1:
            print("You have been saved by Steve Rogers!")
            return True
        elif the_choice == 2 or the_choice == 3:
            state = 4
    if state == 3:
        the_choice = choice("Choose a song to listen to after the hero has brought you safely to the hospital",
                            "Gunpowder and Lead - Miranda Lambert","Before He Cheats - Carrie Underwood","Friends in Low Places - Garth Brooks")
        if the_choice == 1:
            print("Miranda Lambert heard about the accident and came to visit! Unfortunately you passed out in shock and hit your head. You passed away shortly after.")
            return False
        elif the_choice == 2:
            state = 4
        elif the_choice == 3:
            state = 5 
    if state == 4:
        the_choice = choice("You have woken up from your coma to discover that you have superpowers!  Choose a team to join:", "The Avengers","The Justice League","The X-Men")
        if the_choice == 1:
            print("The Avengers have accepted you as a new member!")
            return True
        elif the_choice == 2:
            state = 5
        elif the_choice == 3:
            print("You were murdered by Jean Grey!")
            return False
    if state == 5:
        the_choice = choice("Choose a villain to fight", "Magneto", "Thanos", "Taskmaster")
        if the_choice == 1 or the_choice==3:
            print("Congrats! You have successfully defeated your first villain!")
            return True
        elif the_choice == 2:
            print("You and half the population have turned to dust!")
            return False
        
        

import tkinter as tk
import random
#The Part 1 of Extra Credit is completed. 
#FIRST: Implement and test your Pokemon class below
class Pokemon:
#==========================================
# Purpose: Initializes the class Pokemon with the instance variables, self, species, dex_num, catch_rate, and speed.  
# Input Parameter(s): self-provides reference to class instance, species-type of Pokemon, dex_num-the dex number of the Pokemon
#catch_rate-the catch rate of the Pokemon, and speed-the speed of the pokemon.  
# Return Value(s): None
#==========================================
    def __init__(self,species='',dex_num=0,catch_rate=0,speed=0):
        self.species=species
        self.dex_num=dex_num
        self.catch_rate=catch_rate
        self.speed=speed
#==========================================
# Purpose: Overloads the string method to return the species.  
# Input Parameter(s): self-provides reference to class instance  
# Return Value(s): None
#==========================================
    def __str__(self):
        return str(self.species)


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
#==========================================
# Purpose: Reads pokedex.csv, stores it in a list, has a way to keep track of the remaining balls, has a way to keep track of caught Pokemon,
# and calls the nextPokemon method after createWidgets.  
# Input Parameter(s): self-provides reference to class instance, master-represents the window/display screen
# Return Value(s): None
#==========================================
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.caught=[]
        f=open("pokedex.csv")
        line_list=f.readlines()
        self.pokemon_list=[]
        for item in line_list[1:]:
            item_list=item.split(',')
            pokemon=Pokemon()
            pokemon.dex_num=item_list[0]
            pokemon.species=item_list[1]
            pokemon.catch_rate=item_list[2]
            pokemon.speed=item_list[3].split('\n')[0]
            self.pokemon_list.append(pokemon)
        f.close()
        print("In SafariSimulator init")
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=450)
        master.title("Safari Zone Simulator")
        
        self.balls=30
        
        self.pack()
        self.createWidgets()
        self.nextPokemon()
        #Call nextPokemon() method here to initialize your first random pokemon
        #self.nextpokemon=self.nextPokemon()
#==========================================
# Purpose: Creates a button for throwing the Safari ball, binds it to the throwBall method, creates a Label for the Pokemon sprite image and Catch Probability.
#Extra credit: Creates label for run probability and another label for whether run_catch_Label.  
# Input Parameter(s): self-provides reference to class instance.  
# Return Value(s): None
#==========================================
    def createWidgets(self):
        print("In createWidgets")
        #See the image in the instructions for the general layout required
           



        #"Run Away" button has been completed for you as an example:
        self.runButton = tk.Button(self)
        self.runButton["text"] = "Run Away"
        self.runButton["command"] = self.nextPokemon
        self.runButton.pack(side="bottom")

        #You need to create an additional "throwButton"
        self.throwButton = tk.Button(self)
        self.throwButton["text"] = "Throw Safari Ball ("+str(self.balls)+"left)"
        self.throwButton["command"] = self.throwBall
        self.throwButton.pack(side='top')  

        #A label for status messages has been completed for you as an example:
        self.messageLabel = tk.Label(bg="grey")
        self.messageLabel.pack(fill="x", padx=5, pady=1)

        #You need to create two additional labels:

        #Complete and pack the pokemonImageLabel here.
        self.pokemonImageLabel = tk.Label(bg="white")
        self.pokemonImageLabel.pack(fill="x", pady=1)
        #pokemon=self.nextpokemon
        #dex=nextpokemon.dex_num
        #fname='sprites\/'+str(dex)+('.gif')
        #poke_photo=tk.PhotoImage(file=fname)
        #label=tk.Label(image=poke_photo)
        #label.photo=poke_photo
        #label.pack()
        #Complete and pack the catchProbLabel here.
        self.catchProbLabel = tk.Label(bg="grey")
        self.catchProbLabel.pack(fill="x", padx=5, pady=1)

        #Complete and pack the runProbLabel here.
        self.runProbLabel = tk.Label(bg="pink")
        self.runProbLabel.pack(fill="x", padx=5, pady=1)

        #Complete and pack the run_catch_Label here.
        self.run_catch_Label = tk.Label(bg="white")
        self.run_catch_Label.pack(fill="x", padx=5, pady=1)

#==========================================
# Purpose:Picks a random Pokemon out of 151 possibilities, updates the message label, updates the probability label, PhotoImage object created and saved
# to an instance variable, and image label is updated.
#Extra credit-the run probability label is updated.  
# Input Parameter(s): self-provides reference to class instance 
# Return Value(s): None
#==========================================        
    def nextPokemon(self):
        print('hi',len(self.pokemon_list))
        self.random_pokemon=random.choice(self.pokemon_list)
        dex_num=self.random_pokemon.dex_num
        species=self.random_pokemon.species
        catch_rate=self.random_pokemon.catch_rate
        speed=self.random_pokemon.speed
        print(dex_num, speed, species, catch_rate)
        fname='sprites/'+str(int(dex_num))+'.gif'
        self.poke_photo=tk.PhotoImage(file=fname)
        self.pokemonImageLabel["image"]=self.poke_photo
        self.pokemonImageLabel.photo=self.poke_photo
        

        self.messageLabel["text"]="You have encountered a wild "+str(species)
        

        self.probability_of_catch=min((int(catch_rate)+1),151)/449.5
        self.catchProbLabel["text"]="Your chance of catching it is "+str(int(self.probability_of_catch*100))+"%!"
    
        self.run_prob=(2*(int(speed))/256)
        self.runProbLabel['text']='The chance of '+str(species)+' running is '+str(int(self.run_prob*100))+'%'
        
        print("In nextPokemon")
        
        #This method must:
            #Choose a random pokemon
            #Get the info for the appropriate pokemon
            #Ensure text in messageLabel and catchProbLabel matches the pokemon
            #Change the pokemonImageLabel to show the right pokemon

        #Hint: to see how to create an image, look at the documentation 
        #for the PhotoImage/Label classes in tkinter.
        
        #Once you generate a PhotoImage object, it can be displayed 
        #by setting self.pokemonImageLabel["image"] to it
        
        #Note: the PhotoImage object MUST be stored as an instance
        #variable for some object (you can just set it to self.photo).
        #Not doing this will, for weird memory reasons, cause the image 
        #to not be displayed.
#==========================================
# Purpose: Generates a random number between 0 and 1 and uses that number to see if the Pokemon was caught.  The ThrowButton is then updated to reflect the
#used Safari balls, and an escape message is updated on the message label if the Pokemon was not caught.  Then endAdventure is called if the balls are all used up, or nextPokemon
#is called if the Pokemon was caught.
#Extra credit-Tells the difference between whether the GUI changed because the current one was caught or because it ran away.
# Input Parameter(s): self-provides reference to class instance  
# Return Value(s): None
#==========================================        
    def throwBall(self):
        print("In throwBall")
        
        #This method must:

            #Decrement the number of balls remaining
            #Try to catch the pokemon
            #Check to see if endAdventure() should be called

        #To determine whether or not a pokemon is caught, generate a random
        #number between 0 and 1, using random.random().  If this number is
        #less than min((catchRate+1), 151) / 449.5, then it is caught. 
        #catchRate is the integer in the Catch Rate column in pokedex.csv, 
        #for whatever pokemon is being targetted.
        random_num=random.random()
        if random_num<self.probability_of_catch:
            self.caught.append(self.random_pokemon.species)
            print('hello, caught')
            self.run_catch_Label['text']='The '+str(self.random_pokemon.species)+" was caught!"
            self.nextPokemon()
        else:
            rando=random.random()
            if rando<self.run_prob:
                self.run_catch_Label['text']='The '+str(self.random_pokemon.species)+" has run!"
                self.nextPokemon()
            else:
                self.messageLabel['text']="Aargh! It escaped!"
        self.balls-=1
        self.throwButton["text"]="Throw Safari Ball ("+str(self.balls)+"left)"
        if self.balls<=0:
            self.endAdventure()
        #Don't forget to update the throwButton's text to reflect one 
        #less Safari Ball (even if the pokemon is not caught, it still 
        #wastes a ball).
        
        #If the pokemon is not caught, you must change the messageLabel
        #text to "Aargh! It escaped!"
        
        #Don't forget to call nextPokemon to generate a new pokemon 
        #if this one is caught.
  #==========================================
# Purpose: This method displays message of being out of balls on one label.  It then  displays the number of Pokemon caught and a list of their names on another label.
#All other buttons and labels are removed.  
# Input Parameter(s): self-provides reference to class instance 
# Return Value(s): None
#==========================================      
    def endAdventure(self):
        
        self.messageLabel['text']='You\'re all out of balls, hope you had fun!'
        self.caughtLabel = tk.Label(bg="grey")
        self.caughtLabel.pack(fill="x", pady=1)
        self.caughtLabel.pack()
        if len(self.caught)==0:
            self.caughtLabel['text']="Oops, you caught 0 Pokemon."
        string="You have caught "+str(len(self.caught))+' Pokemon:\n'
        for poke in self.caught:
            string+=poke+'\n'
        self.caughtLabel["text"]=string
    
        self.throwButton.pack_forget()
        self.runButton.pack_forget()
        self.pokemonImageLabel.pack_forget()
        self.catchProbLabel.pack_forget()
        self.run_catch_Label.pack_forget()
        self.runProbLabel.pack_forget()
        print("In endAdventure")
        
        #This method must: 

            #Display adventure completion message
            #List captured pokemon

        #Hint: to remove a widget from the layout, you can call the 
        #pack_forget() method.
        
        #For example, self.pokemonImageLabel.pack_forget() removes 
        #the pokemon image.




#DO NOT MODIFY: These lines start your app
app = SafariSimulator(tk.Tk())
app.mainloop()

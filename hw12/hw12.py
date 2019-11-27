import tkinter as tk
import random

#FIRST: Implement and test your Pokemon class below
class Pokemon:
    def __init__(self,species='',dex_num=0,catch_rate=0,speed=0):
        self.species=species
        self.dex_num=dex_num
        self.catch_rate=catch_rate
        self.speed=speed
    def __str__(self):
        return str(self.species)


#NEXT: Complete the class definition provided below
class SafariSimulator(tk.Frame):
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
        print("In SafariSimulator init")
        #Read in the data file from pokedex.csv at some point here
        #It's up to you how you store and handle the data 
        #(e.g., list, dictionary, etc.),
        #but you must use your Pokemon class in some capacity

        #Initialize any instance variables you want to keep track of

        #DO NOT MODIFY: These lines set window parameters and create widgets
        tk.Frame.__init__(self, master)
        master.minsize(width=275, height=350)
        master.maxsize(width=275, height=350)
        master.title("Safari Zone Simulator")
        
        self.balls=30
        
        self.pack()
        self.createWidgets()
        self.nextPokemon()
        #Call nextPokemon() method here to initialize your first random pokemon
        #self.nextpokemon=self.nextPokemon()

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
        self.messageLabel.pack(fill="x", padx=5, pady=5)

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
        self.catchProbLabel.pack(fill="x", padx=5, pady=5)
        
    def nextPokemon(self):
        print('hi',len(self.pokemon_list))
        self.random_pokemon=random.choice(self.pokemon_list)
        dex_num=self.random_pokemon.dex_num
        species=self.random_pokemon.species
        catch_rate=self.random_pokemon.catch_rate
        speed=self.random_pokemon.speed
        print(dex_num, speed, species, catch_rate)
        fname='sprites/'+str(int(dex_num))+'.gif'
        poke_photo=tk.PhotoImage(file=fname)
        self.pokemonImageLabel["image"]=poke_photo
        self.pokemonImageLabel.photo=poke_photo
        self.pokemonImageLabel.pack()

        self.messageLabel["text"]="You have encountered a wild "+str(species)
        self.messageLabel.pack()

        self.probability_of_catch=min((int(catch_rate)+1),151)/449.5
        self.catchProbLabel["text"]="Your chance of catching it is "+str(int(self.probability_of_catch*100))+"%!"
        self.catchProbLabel.pack()
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

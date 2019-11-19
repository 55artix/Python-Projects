#a)

class Adventurer:
#==========================================
# Purpose: Initializes the Adventurer class, and creates the instance variables
#name, level, strength, speed, power, HP, and hidden.  
# Input Parameter(s): self:self-provides a reference to the class instance.
#name-a string representing the name
#level, strength, speed and power are integers that represent the Adventurer's ability levels.
# Return Value(s): none
#==========================================
    def __init__(self, name='', level=0, strength=0, speed=0, power=0):
        self.name=name
        self.level=level
        self.strength=strength
        self.speed=speed
        self.power=power
        self.HP=6*self.level
        self.hidden=False
#==========================================
# Purpose: Overload the repr() method for the adventurer class so that it returns a string. 
# Input Parameter(s): self:self-provides a reference to the class instance.
# Return Value(s): string in the form of <Name> - HP: <Current HP>
#==========================================
    def __repr__(self):
        return str(self.name)+' - HP: '+str(self.HP)
#==========================================
# Purpose: Takes as a parameter another Adventurer object target and prints a string
#'<Name> can't see <Target/s name>' if the target is hidden.  If the target is not hidden,
#it'll print a string '<name> attacks <target's name> for <damage amount> damage'.
# Input Parameter(s): self:provides a reference to the class instance.
#target-Adventurer object 
# Return Value(s): none
#==========================================
    def attack(self,target):
        if target.hidden==True:
            print(str(self.name)+" can\'t see "+str(target.name))
        else:
            damage=self.strength+4
            target.HP=target.HP-damage
            print(str(self.name)+" attacks "+str(target.name)+" for "+str(damage)+" damage")
#==========================================
# Purpose: Overloads the less than operator to take in another adventurer object
#and returns True or False based on whether the object on the left of the operand is less than
#the object on the right.  
# Input Parameter(s): self:provides a reference to the class instance.
#other-another adventurer object
# Return Value(s): Boolean value based on whether the object on the left of the operand is less than
#the object on the right.   
#==========================================

    def __lt__(self,other):
        if self.HP<other.HP:
            return True
        else:
            return False
       
class Fighter(Adventurer):
#==========================================
# Purpose: The fighter constructor takes the same parameters as its superclass constructor
#and passes them into the superclass constructor, and alters the self.HP=self.level*12
# Input Parameter(s): self:provides a reference to the class instance.
#name-a string representing the name
#level, strength, speed and power are integers that represent the Adventurer's ability levels.
# Return Value(s): none
#==========================================
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.HP=self.level*12
#==========================================
# Purpose: Takes as a parameter another Adventurer object target and prints a string
#'<Name> can't see <Target/s name>' if the target is hidden.  If the target is not hidden,
#it'll print a string '<name> attacks <target's name> for <damage amount> damage'.
# Input Parameter(s): self:provides a reference to the class instance.
#target-Adventurer object 
# Return Value(s): none
#==========================================
    def attack(self,target):
        if target.hidden==True:
            print(str(self.name)+" can\'t see "+str(target.name))
        else:
            damage=2*self.strength+6
            target.HP=target.HP-damage
            print(str(self.name)+" attacks "+str(target.name)+" for "+str(damage)+" damage")

class Thief(Adventurer):
#==========================================
# Purpose: The Thief constructor takes the same parameters as its superclass constructor
#and passes them into the superclass constructor, alters the self.HP=self.level*8, and sets self.hidden=True
# Input Parameter(s): self:provides a reference to the class instance.
#name-a string representing the name
#level, strength, speed and power are integers that represent the Adventurer's ability levels.
# Return Value(s): none
#==========================================
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.HP=self.level*8
        self.hidden=True
#==========================================
# Purpose: Takes as a parameter another Adventurer object target and prints a string
#'<Name> can't see <Target/s name>' if the target is hidden and the self.speed is less than the target.speed.
#If the target is not hidden, the superclass method of the same name will be called.  If the target is hidden but the self.speed
#is not less than the target.speed,
#it'll print a string '<name> sneak attacks <target's name> for <damage amount> damage'.
# Input Parameter(s): self:provides a reference to the class instance.
#target-Adventurer object 
# Return Value(s): none
#==========================================
    def attack(self,target):
        if self.hidden==False:
            Adventurer.attack(self,target)
        elif self.hidden==True:
            if target.hidden==True and self.speed<target.speed:
                print(str(self.name)+' can\'t see '+str(target.name))
            else:
                target.hidden=False
                self.hidden=False
                damage=(self.speed+self.level)*5
                target.HP-=damage
                print(str(self.name)+' sneak attacks '+str(target.name)+' for '+str(damage)+' damage')
class Wizard(Adventurer):
#==========================================
# Purpose: The Wizard constructor takes the same parameters as its superclass constructor
#and passes them into the superclass constructor, and adds another instance self.fireballs_left.  
# Input Parameter(s): self:provides a reference to the class instance.
#name-a string representing the name
#level, strength, speed and power are integers that represent the Adventurer's ability levels.
# Return Value(s): none
#==========================================
    def __init__(self,name,level,strength,speed,power):
        Adventurer.__init__(self,name,level,strength,speed,power)
        self.fireballs_left=self.power
#==========================================
# Purpose: Takes as a parameter another Adventurer object target and calls the superclass method if self.fireballs_leftprints is 0. Otherwise, a string
#str(self.name)+' casts fireball on '+str(target.name)+' for '+str(damage)+' damage' is printed.
# Input Parameter(s): self:provides a reference to the class instance.
#target-Adventurer object 
# Return Value(s): none
#==========================================
    def attack(self,target):
        if self.fireballs_left==0:
            Adventurer.attack(self,target)
        else:
            target.hidden=False
            damage=self.level*3
            target.HP-=damage
            self.fireballs_left-=1
            print(str(self.name)+' casts fireball on '+str(target.name)+' for '+str(damage)+' damage')
#==========================================
# Purpose:Takes adventurer objects adv1 and adv2 as parameters and returns True is adv1 would win, and False otherwise.
# Input Parameter(s): adv1, and ad2 are adventurer objects representing the two objects in the duel.  
# Return Value(s): True if adv1 would win, False otherwise.  
#==========================================
def duel(adv1,adv2):
    if adv1.HP<=0 and adv2.HP>0:
        print(adv1)
        print(adv2)
        print(str(adv2.name)+" wins!")
        return False
    elif adv2.HP<=0 and adv1.HP>0:
        print(adv1)
        print(adv2)
        print(str(adv1.name)+" wins!")
        return True
    elif adv2.HP<=0 and adv1.HP<=0:
        print(adv1)
        print(adv2)
        print("Everyone loses!")
        return False
    else:
        print(adv1)
        print(adv2)
        adv1.attack(adv2)
        if adv2.HP<=0:
            print(adv1)
            print(adv2)
            print (str(adv1.name)+" wins!")
            return True
        else:
            adv2.attack(adv1)
        return duel(adv1,adv2)
#b            
#==========================================
# Purpose:Takes in a single parameter, a list of adventurer objects and pits them against each other until there is a single winner to return. 
# Input Parameter(s): adv_list list of adventurer objects. 
# Return Value(s): The recursive call tournament(adv_list), which will ultimately return the final winner.    
#==========================================    
def tournament(adv_list):
    if adv_list==[]:
        return None
    elif len(adv_list)==1:
        return adv_list[0]
    else:
        sorted_adv_list=sorted(adv_list)
        player1=sorted_adv_list[-2]
        player2=sorted_adv_list[-1]
        duel_result=duel(player1,player2)
        if duel_result==True:
            loser=player2
            index=adv_list.index(loser)
            adv_list.pop(index)
        else:    
            if player1.HP<=0 and player2.HP<=0:
                loser1=player1
                loser2=player2
                index1=adv_list.index(loser1)
                index2=adv_list.index(loser2)
                adv_list.pop(index1)
                adv_list.pop(index2)
            else:
                loser=player1
                index=adv_list.index(loser)
                adv_list.pop(index)
    return tournament(adv_list)

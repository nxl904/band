Bands_Names = ["ZZ Top", "The Eagles", "Slayer", "Metallica"]
global Hired

class Musician(object):
    def __init__(self,sounds):
        self.sounds = sounds
    
    def solo(self, length): 
        for i in range(length): 
            print(self.sounds[i%len(self.sounds)], end=" ")
        print()
        
    
class Bassist(Musician): 
    def __init__(self): 
        super().__init__(["Twang","Thrumb","Bling"])
 
        
class Guitarist(Musician):
    def __init__(self): 
        super().__init__(["Boink", "Bow","Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")


class Drummer(Musician):
    global Hired
    
    def __init__(self):
        super().__init__(["Boom", "Pop","Boom"])
        
    def countdown(self, n):
        print ("Hi everyone we're {}, thanks for coming out tonight let's get rockin!".format(Hired))
        global Go
        Go = {}
        while n > 0: 
            print (n)
            n= n-1
        print ("Go!")
        zero = str(n)
        if zero == "0": 
            Go = True
     
        
    def combust(self):
        print("......BOOOOMMM!")

class Band(object):
   
    def __init__(self):
         super().__init__

    def Hiring(self):
        Hire_Question = input("Do you want to hire a band? ").lower()
        if Hire_Question == "yes" or Hire_Question =="y":
            print("These are the bands:",'\n',*Bands_Names,sep='\n')
        else:
            print("Ok, you're not hiring")
            bnd.Hiring()
#Need a loop in the Choice method. This is a point of failure 
    def Choice(self):
        global Hired
        Band_Choice = input('\n'"Which band do you want to hire? ")
        if Band_Choice == "ZZ Top" or Band_Choice =="The Eagles" or Band_Choice == "Slayer" or Band_Choice == "Metallica":
            Hired = (Band_Choice)
        else:
            print("You didn't enter a bands name")
            bnd.Hiring()

    def Fire(self):
        global Hired
        global Loopy
        global Empty
        Loopy = " "
        Empty = " "
        Band_Performance = input("Is {} rocking hard? (y/n) ".format(Hired)).lower()
        if Band_Performance == "yes" or Band_Performance == "y":
            print("Glad to hear it's working out!")
        elif Band_Performance == "no" or Band_Performance == "n" :
            Fired = Hired
            Hired = Empty
            print("No problem, we fired those clowns!")
            Loopy = True
        else:
            print("You didn't enter 'yes' or 'no'")

    
    def Loop(self):
        while Loopy == True:
            bnd.Hiring()
            bnd.Choice()
            bnd.Fire()
            
    
    def post_countdwn(self): 
        if Go == True:
           b = Bassist()
           b.solo (3)
           g = Guitarist()
           g.solo (3)
           d = Drummer()
           d.solo (3)
        else:
            print ("cool")


bnd = Band()
bnd.Hiring()
bnd.Choice()
bnd.Fire()
bnd.Loop()

drm = Drummer()
drm.countdown(4)

bnd.post_countdwn()
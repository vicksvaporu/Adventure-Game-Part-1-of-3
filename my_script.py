import sys
import time

# This bit of code was taken from a thred on https://stackoverflow.com/questions/20302331/typing-effect-in-python

def printSlow(str):
    for char in str:
        time.sleep(.06)
        sys.stdout.write(char)
        sys.stdout.flush()

#end of imported function 


# here is the general input assertion lists that I will use to allow players to choose options: either A or B
A_or_B = ['A', 'a', 'B', 'b']
A = ['a', 'A']
B = ['b', 'B']

# through the game, items will be added to these lists. they represent what the player has in his/her possession
possessions = []
sword = []
blessings = []



# this just prints the introduction to the game
def awakeningScene():
    printSlow('''
    “...wake up, the time has come...”
    
    
    You awaken in a humid cavern surrounded by a rounded wall of glazed stone. 
    There’s not much to see other than a flickering candle next to you on a small stool. 
    The entrance to the cavern is covered by a thick curtain of fabric. 
    Sunlight slips through the opening and gives the cavern a warm glow. 
    You rise to your feet, you feel a little stiff but manage to walk to the entrance and step outside the curtain. 
    A cool breeze ruffles your thin shirt and short trousers. 
    You notice you have no shoes. 
    When your eyes adjust to the bright light,
    you notice you stand at the top of a large hill overlooking a small village on a plateau to the South. 
    To the North, you can see a vast landscape: 
    in the middle of open plains in the distance, 
    a decrepit castle is surrounded by aggressive lightening clouds, 
    daring anyone to come close. 
    ''')
    
# the first function that allows players a choice    
def outOfCavern():
    direction = ''
    while direction not in A_or_B: #similar to the next functions, this throws the player in a loop until they pick A or B
        direction = input('''
        A: head to the village
        B: head to the castle
        ''')
        if direction in A:
            village()   #redirects player to another function
        elif direction in B:
            printSlow('''
            You go down the hill and come across the edge of the plateau.
            It’s a 100 foot vertical climb down.
            ''')
            offPlateau()  #redirects player to a different function if this option is chosen
    
    return direction


def offPlateau():
    direction_2 = ''
    while direction_2 not in A_or_B:
        direction_2 = input('''
        A: head to the village instead
        B: try to climb down
        ''')
        if direction_2 in A:
            village()
        elif direction_2 in B:
            printSlow('''
            You lower yourself to the edge of the plateau trying to maintain your grip. 
            You successfully climb down 5 feet when you lose your footing and plummet to your death. 
            Congrats. What did you expect?
            ''')
            quit()
              # Here, the player dies and they will be exited out of the code. I did not add an option to "play again"
    return direction_2


def village():
    printSlow('''
    You head down to the small village. 
    A small thicket of woods surrounds the place and for some reason,
    you feel at peace. 
    Upon closer inspection, you notice that its mostly residential. 
    A steady river gurgles merrily through the village. 
    You look around trying to remember where you are but you soon realize you don’t recall anything; 
    not even your own name. 
    A voice woke you up, but no one was there when you opened your eyes. 
    You weave your way through the houses and spot a building nestled between ancient trees
    that stands taller than the rest. 
    Steps lead to the entrance of a house with neat bamboo walls and a high ceiling. 
    Tall open windows decorate the walls and a balcony wraps around the building.''')
    village_path = ''
    while village_path not in A_or_B:
        village_path = input('''
        A: Go to the house 
        B: Find a way out of the village
        ''')
        if village_path in A:
            mysteriousWoman()
        elif village_path in B:
            printSlow('''
            As you turn around,
            you find yourself looking into the large golden eyes of a giant grey wolf. 
            It growls softly at you but just heads to the house and silently slips through the door.
            ''')
            secondChance()
    return village_path



def mysteriousWoman():
    printSlow('''
    You head up the stairs to the house and try the door. 
    Surprisingly, it opens to a large room with redwood floors. 
    Before you can take in the entire room, 
    you notice a young woman sitting on a pedestal with her legs crossed at the far end of the dim room. 
    You notice she is turned your way. 
    Her long brown hair neatly twisted into a thick braid and simple saffron yellow jumpsuit look familiar, 
    but you cannot seem to grasp the memory. 
    There’s nothing particularly special about her other than the red cloth wrapped around her eyes.
 
        “Well, it definitely is about time. 
        I am sure you’re extremely confused and don’t remember what happened,” 
        
    her low voice seemed to be your head. 
    
        “I suppose I should start from the very beginning, 
        and please do not interrupt...I do not have much time. 
        Our kingdom of Vikenrye has a legend as old as the land itself. 
        Light and Darkness are cursed to fight for eternity, 
        reborn time and time again in a never-ending cycle. 
        I am sure you saw the castle in the distance-- 
        a constant reminder of what we failed to do one hundred years ago. 
        The Lady of Nothing’s threat to succumb the world in chaos hangs above us, 
        and she has almost succeeded. 
        To ensure she is not challenged again, she seeks the power of Light...
        the only power that can seal her away, for she cannot die. 
        She has searched a century for the missing piece but alas you are here,” 
    
    she smiles warmly at you, 
    
        “I hid you away until you were ready to challenge Nothing again for only the Hero of Light can defeat her. 
        Sealing you away was the only way to save you from death, 
        your wounds were far too severe and your mind far too weak. 
        You'll need a sword of Moonglass. 
        Then you need it blessed by the Masters of Truth, Wisdom, and Power. 
        That is all I will tell you, the rest is up to you”.
 
    She whistled softly and soft fur brushed your arm as a giant grey wolf took its place next to the young woman.
        
        “I exchanged my sight for one hundred years of youth so I could send you off when you were finally ready, 
        and that time is nearly over...
        Apeira is all I have to remember the life of long ago but her days end with mine.” 
    
    The woman strokes her wolf’s fur and whispers indistinctly in its ear. 
    She motions to the door, 
        
        “Apeira will guide you off the plateau”.

    As you reach the doorway the young woman speaks again, 
        
        “I am sure you’ll find this useful.” 
        
    She tosses you a small satchel and inside you find:
    a fresh change of clothes, 
    boots, 
    a bag of one hundred coins, 
    and a small dagger.
    
        "Good luck Hero of Legend...do not disappoint...”
        
        ''')
    possessions.append('clothes')  # items are added to the player's inventory!
    possessions.append('money')
    possessions.append('dagger')
    withApeira()
    return


def secondChance():
    pls_go_to_house = ''
    while pls_go_to_house not in A_or_B:
        pls_go_to_house = input('''
        A. follow the wolf
        B. pretend you saw nothing and try to find a way off the plateau
        ''')
        if pls_go_to_house in A:
            mysteriousWoman()
        elif pls_go_to_house in B:
            printSlow('''
            You continue past the house and find a narrow path that leads to the other end of the plateau. 
            There, you see a steep slope leading to the ground below. 
            You make your way down slowly but you manage to make it to the bottom. 
            Your bare feet hurt and each step is a sharp pain up your leg.
            That flimsy shirt you're wearing won't offer any warmth. 
            There’s no way to go back up so your best bet is to walk and hope to find a main road.''')
            oldLady()
    return pls_go_to_house




def oldLady():
    printSlow('''
    You’ve walked for what you think is an hour.
    Your feet are starting to bleed.
    Up the road in the distance you see an elderly woman next to a broken down cart trying to calm her horse. 
    She sees you approaching, 
        “Oi! Would you be a dear and give an old lady a hand?”
    You see no harm in helping her. Actually, it’s a good time to ask questions. 
    You manage to put her carriage wheel back on the spokes and she’s able to be on her way. 
        
        “Thank you, young one.
         I don’t have much to give my thanks but why are you dressed in rags?? 
         I have some of my son’s old clothes you could have and this,” 
    
    she hands you single peculiar gold coin. 
        
        “Its a coin from before the Lady of Nothing inhabited that castle you can see across the plains. 
         I have no use for it now.” 
         
    She hands you a bundle of clothes and starts to walk away.
    ''')
    possessions.append('clothes')    # these items are added to inventory
    possessions.append('money')
    ask_questions = ''
    while ask_questions not in A_or_B:
        ask_questions = input('''
        A: Stop her and ask her about the Lady of Nothing
        B: Ask about where you are
        ''')
        if ask_questions in A:
            printSlow('''
            “The Lady of Nothing? 
            My! Have you been asleep for the past century? 
            One hundred years ago she nearly succumbed this kingdom into darkness. 
            My father told me that there is only one person who could defeat her: 
            a grand hero with a Moonglass sword blessed by the Masters of Courage, Power, and Wisdom. 
            Now that story is almost legend. 
            My father said the hero was put into a deep sleep and hidden away somewhere until the time came. 
            I’m not sure what to believe anymore...
            Well, goodbye young one! And good luck!!”
            ''')
            crossRoads()
        if ask_questions in B:
            printSlow('''
            “Are you a lost traveler? 
            You’re in the kingdom of Vikenrye of course! 
            It would be a lovely place if it wasn’t for the Lady of Nothing threatening to overtake the kingdom. 
            There is an old legend of a hero
            with a Moonglass sword blessed by the Masters of Power, Truth, and Wisdom 
            who will one day relieve this land of the threat of the Lady of Nothing. 
            I wonder if that is even possible...dear me! 
            I rambled on! 
            I must be on my way, good bye!”''')
            crossRoads()
    return ask_questions
    
    
    
def withApeira(): #this is just a fun code that is not necessary but lets you pet the wolf
    printSlow('''
    Apeira heads out the door and behind the house. 
    You see a dirt slope that heads to the ground below. 
    Before going down you put on your new clothes and boots. 
    They look well worn fit your body well and you wonder if it was the clothing you wore a century ago. 
    You strap the dagger to your thigh and shoulder the satchel.
    When you reach the bottom of the slope,
    Apeira nudges your shoulder, as if motioning that that’s as far as she’ll go.
    Her eyes could tell you the stories you've forgotten.
    You get the warm feeling that she has been an important part of your life from the start,
    but you still remember nothing.
    ''')
    off_to_adventure = ''
    while off_to_adventure not in A_or_B:
        off_to_adventure = input('''
        A. Pet the good girl
        B. Head in the general direction 
        ''')
        if off_to_adventure in A:
            printSlow('''
            You pet Apeira. 
            Her thick fur is the softest thing you have ever touched.
            ''')
            crossRoads()
        if off_to_adventure in B:
            crossRoads()
    return off_to_adventure


##############################################################################################
def sword(int):
    if int == 3:
        output = 'You can go challenge the Lady of Nothing!'
    else:
        output = 'You are not strong enough to defeat the Lady of Nothing. To be continued....'
    return output
##################################################################################################


def crossRoads(): #this is where the diverted paths converge and where the code ends
    printSlow('''
    You walk for a while in a general direction and find a well-worn road. 
    You follow it until you get to a crossroads. 
    A sign at the fork reads:
    
              <— Vikenrye Palace & Royal Grounds
                         Buttermilk Valley Village —>
    ''')
    printSlow(sword(0))
    return


    
awakeningScene()
outOfCavern()


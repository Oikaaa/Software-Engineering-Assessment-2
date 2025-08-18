from Classes.Locations import Location
from Classes.Characters import Character
from Classes.Characters import NPC
from Classes.Characters import Enemy
from Classes.Locations import Maze
import time
import os
import random
from Classes.Locations import Zone
player = Character('Guest')
player.add_inventory('Bright Echo')

# Please NOTE that don't let the character ABILITY WASTED AND INVENTORY (iykyk)
TheListener = NPC("The Listener", "A mouthless nun of hymns.")
CorruptedSurvivor = NPC("Corrupted Survivor", "A mouthless nun of hymns.")
SilentZone = Location('The Hollow Choir Zone', '“Some songs end in silence. Others end in teeth.”\n | The ground is made of fractured pews, arranged in endless rows, tilting upward into darkness.\n | Above you, the ceiling arches away into a cavern of bone-white stalactites that drip with black, ink-like water.\n | The Listener, is what dead pray for', 'Rythm is what feed The Listener... Destroy all the rythms and devour it soul with darkness...', 'DESTROY THE HOLLOW OF CHOIR')
SilentZone.add_character(TheListener)
SilentZone.add_character(CorruptedSurvivor)

Safe_Haven = Zone("Safe Havens", "The air smells of coal and damp stone. Beyond the faded yellow safety line, the voices of the outside world fall silent, as if afraid to cross.", None, None) #Player start here
Choir_Fields = Zone("Choir Field", "An endless field of pale grass, unmoving in a dead wind. Weather-worn choir stands dot the land, each holding a rotting hymnal that hums faintly when touched. The fragments and ehoes within can form something far more dangerous.", None, None) # Create a holy bible using the fragments and echoes
Echo_Zone = Zone("Echo Zone", "A vast black-stone amphitheater where every sound returns softer and wrong. Faintly glowing crystals pulse like alien hearts, guiding you to gather every last echo before something else does.", None, None) # Use that Item to collect all the echo
Silent_Zone = Zone("Silent Zone", "A ruin where dust hangs in the air and no wind stirs. The Listener patrols here, drawn to the smallest sound. Survive by moving in the rare, precious moments of silence.", TheListener, None) #The Listener is here, kill it by using all the item in inventory (in order)
Hollow_Zone = Zone("Hollow Zone", "A cathedral of bone-white stone and shattered pews. Shadows ripple with unseen life. Here, Dark and Light Echoes may be joined into something new.", None, None) #Combine Dark Echo and Light Echo to form a new item
#IF YOU ALREADY HAD THE DARK ECHO YOU CAN SKIP ALL THESE ROOM
Dark_Zone = Zone("Dark Zone", "A black abyss of jagged stone where whispers crawl under your skin. The Dark Echo waits, feeding on fear and hesitation.", None, None) #Receive Dark Echo
Light_Zone = Zone("Light Zone", "A chamber of endless mirrored walls bathed in searing light. Every step exposes what hides within you, and the Light will burn away falsehoods.", None, None) #You use Light to UNlock the Secret Zone
Secret_Zone = Zone("Secret Zone", "A hidden sanctum of shifting corridors and looping halls. Solve the riddle that reshapes the room to earn the right to enter the Dark Zone.", None, None) # Solving Secret Zone To access Dark Zone

def randomStructure():
    Zones = [Choir_Fields, Echo_Zone,Hollow_Zone,Dark_Zone,Light_Zone,Secret_Zone] #Never take Safe Havens and Silent Zone'

    #RESET ALL LINKED ZONES
    for zone in Zones:
        zone.linkedZone = []
    Safe_Haven.linkedZone = []
    Silent_Zone.linkedZone = []

    #4 Rooms lined to the Starting point
    for i in range(4): #0, 1, 2, 3
        Safe_Haven.add_zone(Zones.pop(random.randint(0,len(Zones)-1))) #E, W, N, S
    #link a room to the west room from the starting point
    RemainZone1 = Zones.pop(random.randint(0,1))
    RemainZone2 = Zones.pop(0)
    #WEST FROM START
    for i in range(4):
        if i == 0: #East
            Safe_Haven.linkedZone[1].add_zone(Safe_Haven) #[English translate] Add Safe Haven zone to the EAST of THE ROOM THAT IS LINKED TO THE WEST of Safe Haven
        elif i == 2: #North
            Safe_Haven.linkedZone[1].add_zone(RemainZone1) #[English translate] Add the first Remain Zone to the North of THE ROOM THAT IS LINKED TO THE WEST of Safe Haven
        else:#West and South
            Safe_Haven.linkedZone[1].add_zone(None) #Add none to the other direction
    #NORTH FROM START
    for i in range(4):
        if i == 3: #South
            Safe_Haven.linkedZone[2].add_zone(Safe_Haven) #[English translate] Add Safe Haven zone to the SOUTH of THE ROOM THAT IS LINKED TO THE NORTH of Safe Haven
        elif i == 1: #West
            Safe_Haven.linkedZone[2].add_zone(RemainZone1) #[English translate] Add the first Remain Zone to the WEST of THE ROOM THAT IS LINKED TO THE NORTH of Safe Haven
        else:#West and South
            Safe_Haven.linkedZone[2].add_zone(None) #Add none to the other direction
    #SOUTH FROM START
    for i in range(4):
        if i == 2: 
            Safe_Haven.linkedZone[3].add_zone(Safe_Haven) #Add to north
        else:
            Safe_Haven.linkedZone[3].add_zone(None) #Add none to the other direction
    #EAST FROM START
    for i in range(4):
        if i == 1: 
            Safe_Haven.linkedZone[0].add_zone(Safe_Haven) 
        elif i == 0: 
            Safe_Haven.linkedZone[0].add_zone(RemainZone2) 
        else:
            Safe_Haven.linkedZone[0].add_zone(None) #Add none to the other direction

    RemainZone1.add_zone(Safe_Haven.linkedZone[2])
    RemainZone1.add_zone(None)
    RemainZone1.add_zone(None)
    RemainZone1.add_zone(Safe_Haven.linkedZone[1])

    for i in range(4):
        if i == 1: 
            RemainZone2.add_zone(Safe_Haven.linkedZone[0])
        elif i == 2:
            RemainZone2.add_zone(Silent_Zone)
        else:
            RemainZone2.add_zone(None) #Add none to the other direction

    Silent_Zone.add_zone(None)
    Silent_Zone.add_zone(None)
    Silent_Zone.add_zone(None)
    Silent_Zone.add_zone(RemainZone2)
        
def direction(dir):
    if dir == 0:
        return "East"
    elif dir == 1:
        return "West"
    elif dir == 2:
        return "North"
    elif dir == 3:
        return "South"

LightZone = False
SecretZone = False
DarkZone = False
HollowChoir = False
EchoZone = False
ChoirField = False
SilentZone = False
def Safe_Haven_Function():
    print("Creatures can't cross the zone, I am safe here. At least I can easily accessed nearby Zone.")
    return
    
def Light_Zone_Function():
    print('')
    if LightZone is False:
        print('The room filled with light that shine through every sounds')
        time.sleep(2)
        print('You are holding it, you are holding the power')
        time.sleep(2)
        print('This is the beginning after the end')
        user_response = input('Would you like to use Bright Echo to unlock a hidden room?\n[1] Yes\n[2] No\n>>> ')
        if user_response == "1":
            print("The light absorbed the Echo. The zone started to rumble, wall collapsed and falling, bouncing back and one d-")
            time.sleep(2)
            print("You wake up in the debrises the Bright Echo is in your hand, trying to tell you something.")
            return True
        else:
            print("Are you sure about that? Don't worry you can comeback anytime when you are ready.")
            return False
    else:
        print("I've been here before...")
        return True

def Secret_Zone_Function():#Puzzle 
    if SecretZone is False:
        if LightZone is True:
            print('"Oh, hi there!"')
            time.sleep(2)
            print('???')
            time.sleep(2)
            print('"Im over here"')
            time.sleep(2)
            print("Suddenly a voice came from darkness")
            time.sleep(2)
            print("A figure that is completely covered in darkness, look like a person with two shadows.")
            time.sleep(2)
            print('"I know it is weird but I know what you are looking for')
            time.sleep(2)
            print('"I can see that you are holding one of the echo, and you are trying to find the rest.')
            time.sleep(2)
            print('"Well, unlucky for you, you have missed your opportunity to get it before."')
            time.sleep(2)
            print('"I am pretty sure it had appeared in the Flooded Bridge scenario before, but look like you had missed it."')
            time.sleep(2)
            print('"I cant help you with that"')
            time.sleep(2)
            print('"But I can give you a key, a key to open a room that you might want."')
            time.sleep(2)
            print('"I not gonna ask much, just answer a feel questions from me, and I will give you the key to that room"')
            time.sleep(2)
            print('"Bet?"')
            userResponse2 = input("Accept the challenge?\n[1] Yes\n[2] No\n>>> ")
            if userResponse2 == "1":
                print('"Alright..."')
            else:
                return print('"...')
            print('')
            # Riddle 1
            next_step = False
            while next_step is False:
                print('"Im tall when Im young, Im short when Im old. what am I?"')
                userResponse2 = input('C _ _ _ _ _\n>>> ').lower()
                if userResponse2 == "candle" or userResponse2 == "andle":
                    print('"Nice try, that was easy."')
                    next_step = True
                else:
                    print('"Well, try again."')
            print('')
            time.sleep(2)
            # Riddle 2
            next_step = False
            while next_step is False:
                print('"Pronounced as one letter, And written with three, two letters there are, and two only in me. I’m double, I’m single, I’m black blue and gray, I’m read from both ends, and the same either way. What am I?"')
                userResponse2 = input('_ _ _\n>>> ').lower()
                if userResponse2 == "eye":
                    print('"Well played."')
                    next_step = True
                else:
                    print('"Well, try again."')
            print('')
            time.sleep(2)

            # Riddle 3
            next_step = False
            while next_step is False:
                print('"David`s father has three sons: Snap, Crackle and _____?"')
                userResponse2 = input('>>> ').lower()
                if userResponse2 == "david":
                    print('"Alright, this one will be harder."')
                    next_step = True
                else:
                    print('"Well, try again."')
            print('')
            time.sleep(2)

            # Riddle 4
            next_step = False
            while next_step is False:
                print('"Where is the only place where today comes before yesterday?"')
                userResponse2 = input('D _ _ _ _ _ n _ _ y\n>>> ').lower()
                if userResponse2 == "dictionary":
                    print('"I see, you are smart, last one."')
                    next_step = True
                else:
                    print('"Well, try again."')
            print('')
            time.sleep(2)

            # Riddle 5
            next_step = False
            while next_step is False:
                print('"What is 3/7 chicken, 2/3 cat, and 2/4 goat?"')
                userResponse2 = input('>>> ').lower()
                if userResponse2 == "chicago":
                    print('"Well, you beat me."')
                    next_step = True
                else:
                    print('"Well, try again."')

            print('"It was pretty good, here is your key, go and destroy The Listener."')
            print('The corrupted survivor gave you a corrupted, dark key.')
            print('[...]')
            return True
        else:
            return False
    else:
        print("I've been here before...")
        return True

def Dark_Zone_Function():#Dialogue, reset map # A KEY
    if SecretZone is True:
        if "Dark Echo" not in player.inventory:
            #Code here
            print("You've entered the Area")
            time.sleep(2)
            print("Opposite from Light Zone, this place is filled with darkness in every corner of the zone")
            time.sleep(2)
            print("But nothing can be darker than an orbs in centre")
            time.sleep(2)
            print("A strong and power force trying to devour your soul, pulling everything toward it")
            time.sleep(2)
            print("You are scared")
            time.sleep(2)
            print("Terrified,")
            time.sleep(2)
            print("Trying to runaway from the dark hole.")
            time.sleep(2)
            print("But it was too late")
            time.sleep(2)
            print("You can feel every muscles, tissues on your face slowly stretched out")
            time.sleep(2)
            print("Your eyes popped out of its skull, pulling out your brain and everything blood vessels in it,")
            time.sleep(2)
            print("Your body shattered into pieces that were stretch like a spaghetti,")
            time.sleep(2)
            print("You can feel it, but you can't scream")
            time.sleep(2)
            print("All you see, is just pure darkness.")
            print('')
            time.sleep(2)
            print("A light stare into your eyes, where it should not be there anymore.")
            time.sleep(2)
            print("You are awake from the Safe Heaven, the beginning")
            time.sleep(2)
            print("Thinking everything is just imagination")
            time.sleep(2)
            print("But it's not")
            time.sleep(2)
            print("You feel like the structure of the place had changed, it was not the same as the beginning")
            time.sleep(2)
            print("And in your hand, holding tightly to the Dark Echo")
            time.sleep(1)
            print("[YOU'VE OBTAINED DARK ECHO]")
            player.add_inventory("Dark Echo")
            randomStructure()
            return True
        else:
            print("You already had the Echo, why do you need twice?")
            return False
    else:
        print("You are not ready yet.")
        return False

    
def Hollow_Choir_Function(): #Combine Echo
    if HollowChoir is False:
        print('')
        print('"The shadow and light had balanced out the universe for a millenia, the formation create a strong power of lives that gives living to things."')
        if "Bright Echo" in player.inventory and "Dark Echo" in player.inventory:
            time.sleep(2)
            print("There is nothing here, just a deep and deadly void.")
            time.sleep(2)
            print("You can feel a strong power come from nowhere, the echoes keep vibrating non-stop, trying to speak up something.")
            time.sleep(2)
            print("Suddenly, a voice telling you a story")
            time.sleep(2)
            print("Everthing started of nothing, literally nothing")
            time.sleep(2)
            print("Then, a dark matter came out from the void devour everything that is on its path.")
            time.sleep(2)
            print("However, it was not the only matter in this empty space,")
            time.sleep(2)
            print("A strong bright light, approaching towards it, trying to stop it from eating all the sound of this cruel world.")
            time.sleep(2)
            print("Finnaly, they absorbed each other, giving and balancing out everything in the space, creating the first living for the place of nothingness.")
            time.sleep(2)
            print("You are carrying one of them, you are the choosen one")
            time.sleep(2)
            print("Would you like to combine the Echo, to receive a more extremely powerful orbs?")
            userResponse3 = input('[1] Yes\n[2] No\n>>> ')
            if userResponse3 == "1":
                print("The orbs combined, an invincible compression forces push them into a single Echo")
                time.sleep(2)
                print("It was darkly shining, that can kill your eyes under a second if you look at its darkness.")
                time.sleep(1)
                print("[YOU'VE OBTAINED THE MATTERS OF THE BEGINNING]")
                player.remove_inventory("Dark Echo")
                player.remove_inventory("Bright Echo")
                player.add_inventory("The Matter")
            else:
                print('[...]')
                return False
            return True
        else:
            print("You are missing one of the cores...")
        return False
    else:
        print("I've been here before...")
        return True


def Echo_Zone_Function(): # AI Generated
    # Collect Echo Minigame
    if "The Matter" in player.inventory:
        print("\n--- Echo Zone ---")
        print("The place is ruined...")
        time.sleep(2)
        print("Thousands of floating spirits drift in limitless space.")
        time.sleep(2)
        print("This is the source of echoes, kept by the Listener for consumption.")
        time.sleep(2)
        print("But if it consumes too many, it melts into pieces under the heat of past lives.")
        time.sleep(2)
        print("\nYour task: Collect at least 10 echoes.")
        time.sleep(2)
        print("The Matter in your possession will attract echoes towards you.\n")

        echoes_collected = 0
        attempts = 0

        while echoes_collected < 10 and attempts < 20:  # Limit attempts to avoid infinite loop
            time.sleep(1)
            attempts += 1
            # Chance to collect between 0–3 echoes each attempt
            gained = random.choice([0, 1, 2, 3])
            echoes_collected += gained
            print(f"Attempt {attempts}: You gained {gained} echoes. Total = {echoes_collected}")

        if echoes_collected >= 10:
            print(f"\n[YOU'VE OBTAINED {echoes_collected} LIFELESS ECHOES]")
            player.add_inventory(f"Lifeless Echoes")
            return True, echoes_collected
        else:
            print("\nYou failed to collect enough echoes. The spirits scatter away...")
            return False, 0

    else:
        print("You are not ready yet. The Matter is required to attract the echoes.")
        return False, 0

def Choir_Fields_Function(echoes):#Holy Bible
    print('')
    if "Lifeless Echoes" in player.inventory:
        print(f'"{echoes} Echoes? That`s alot"')
        time.sleep(2)
        print('"You may don`t know me, but you don`t have to."')
        time.sleep(2)
        time.sleep(2)
        print(f'"Just lend me {echoes} Echoes and all your fragments, I will give you something better"')
        time.sleep(2)
        print('* You gave all your fragments and echoes to the voice')
        print('')
        time.sleep(2)
        print('It gave back all the items in a strange bag')
        time.sleep(2)
        print('Something in it shining through all the item')
        time.sleep(2)
        print('A glory golden light came from a book.')
        print("[YOU'VE OBTAINED HOLY BIBLE]")
        player.add_inventory("Holy Bible")
        return True
    else:
        return False

def Silent_Zone_Function():
    print('Your last stage of the journey')
    time.sleep(2)
    print('A creature with thousand of ears growling in the corner of thr room')
    time.sleep(2)
    print('It was waiting for someone to tell it a story')
    time.sleep(2)
    print('A story that can`t never been told')
    if ChoirField == True:
        print('It noticed your presense')
        time.sleep(2)
        print('Slowly standing up from debris comming towards you')
        time.sleep(2)
        print('You have no where to run, you have to fight for your life.')
        time.sleep(2)
        print('\nBut killing the Listener is not just as usual as the other')
        time.sleep(2)
        print('You have to do it in order')
        time.sleep(2)
        print('There is no record about how it will die, but there is a way that will guaranteed that it will never be able to comeback')
        time.sleep(2)
        print('Blind it with the light, then let it consume the orbs. When it was still being blinded, swallow it with the darkness, and tell it the story that it always waiting for.')
        time.sleep(2)
        print('Good Luck.')
        print('\n')

        next2 = False
        while next2 is not True:
            print("How would you like to start first?")
            for item in range(len(player.inventory)):#Print all the items
                print(f"[{item + 1}] {player.inventory[item]}")
            choosing_weapon = input('>>> ')#Choose weapon

            if choosing_weapon == "1":
                print("The Listener was binded by the light, it is a good time to make a move.")
                next2 = True
            else:
                print("The creature still standing.")
        print('')
        time.sleep(2)

        next2 = False
        while next2 is not True:
            print("How would you like to start first?")
            for item in range(len(player.inventory)):#Print all the items
                print(f"[{item + 1}] {player.inventory[item]}")
            choosing_weapon = input('>>> ')#Choose weapon

            if choosing_weapon == "2":
                print("The creature devour all the echoes, it is dying in pain, the heat is slowly smelt the listening from inside out.")
                next2 = True
            else:
                print("The creature still standing.")
        print('')
        time.sleep(2)
        next2 = False
        while next2 is not True:
            print("How would you like to start first?")
            for item in range(len(player.inventory)):#Print all the items
                print(f"[{item + 1}] {player.inventory[item]}")
            choosing_weapon = input('>>> ')#Choose weapon

            if choosing_weapon == "1":
                print("The darkness is swallowing the creatire, trapping it in a prison that it can`t escape.")
                next2 = True
            else:
                print("The creature is dying painful, but soon it will regenerate, try something else.")
        print('')
        time.sleep(2)
        next2 = False
        while next2 is not True:
            print("How would you like to start first?")
            for item in range(len(player.inventory)):#Print all the items
                print(f"[{item + 1}] {player.inventory[item]}")
            choosing_weapon = input('>>> ')#Choose weapon

            if choosing_weapon == "3":
                print("The will from the book gave you something that you had lost")
                time.sleep(2)
                print("You`re mouth has comeback where it used to be.")
                time.sleep(2)
                print("Your words stabbed through the ears of the creature")
                time.sleep(2)
                print("It is bleeding, flooding the whole room with flesh blood")
                next2 = True
            else:
                print("One more chance.")
        return True
    else:
        print("[You are not ready yet]")
        return False

    
randomStructure()
currentZone = Safe_Haven
previous_zone = currentZone
echoes_collected = 0
while SilentZone is not True:
    try:
        print('')
        currentZone.inform_zone()
        for zoneDir in range(len(currentZone.linkedZone)):#Print direction guide
            if currentZone.linkedZone[zoneDir] is not None:
                print(f'"{currentZone.linkedZone[zoneDir].print_name()}" is at {direction(zoneDir)}') #Print in4

        previous_zone = currentZone
        userResponse = input('\n[W] North \n[A] West \n[S] South \n[D] East\n[E] Examine the area\n>>> ').lower()
        if userResponse == "d":
            currentZone = currentZone.linkedZone[0] #East
        elif userResponse == "a":
            currentZone = currentZone.linkedZone[1] #West
        elif userResponse == "w":
            currentZone = currentZone.linkedZone[2] #North
        elif userResponse == "s":
            currentZone = currentZone.linkedZone[3] #South
        elif userResponse == "e":
            if currentZone == Safe_Haven:
                Safe_Haven_Function()
            elif currentZone == Light_Zone:
                LightZone = Light_Zone_Function()
            elif currentZone == Secret_Zone:
                SecretZone = Secret_Zone_Function()
            elif currentZone == Dark_Zone:
                DarkZone = Dark_Zone_Function()
                if DarkZone == True:
                    currentZone = Safe_Haven
            elif currentZone == Hollow_Zone:
                HollowChoir = Hollow_Choir_Function()
            elif currentZone == Echo_Zone:
                Echo_Zone, echoes_collected = Echo_Zone_Function()
            elif currentZone == Choir_Fields:
                ChoirField = Choir_Fields_Function(echoes_collected)
            elif currentZone == Silent_Zone:
                SilentZone = Silent_Zone_Function()
        else:
            print("Invalid Input")
    except:
        print("Something went wrong.")
        currentZone = previous_zone
    time.sleep(1)

#END DIALOGUE
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

# Please NOTE that don't let the character ABILITY WASTED AND INVENTORY (iykyk)
TheListener = NPC("The Listener", "A mouthless nun of hymns.")
CorruptedSurvivor = NPC("Corrupted Survivor", "A mouthless nun of hymns.")
SilentZone = Location('The Hollow Choir Zone', '“Some songs end in silence. Others end in teeth.”\n | The ground is made of fractured pews, arranged in endless rows, tilting upward into darkness.\n | Above you, the ceiling arches away into a cavern of bone-white stalactites that drip with black, ink-like water.\n | The Listener, is what dead pray for', 'Rythm is what feed The Listener... Destroy all the rythms and devour it soul with darkness...', 'DESTROY THE HOLLOW OF CHOIR')
SilentZone.add_character(TheListener)
SilentZone.add_character(CorruptedSurvivor)

Safe_Haven = Zone("Safe Havens", "The air smells of coal and damp stone. Beyond the faded yellow safety line, the voices of the outside world fall silent, as if afraid to cross.", None, None) #Player start here
Choir_Fields = Zone("Choir Field", "An endless field of pale grass, unmoving in a dead wind. Weather-worn choir stands dot the land, each holding a rotting hymnal that hums faintly when touched. The fragments and ehoes within can form something far more dangerous.", "Char", "Item") # Create a holy bible using the fragments and echoes
Echo_Zone = Zone("Echo Zone", "A vast black-stone amphitheater where every sound returns softer and wrong. Faintly glowing crystals pulse like alien hearts, guiding you to gather every last echo before something else does.", None, None) # Use that Item to collect all the echo
Silent_Zone = Zone("Silent Zone", "A ruin where dust hangs in the air and no wind stirs. The Listener patrols here, drawn to the smallest sound. Survive by moving in the rare, precious moments of silence.", TheListener, None) #The Listener is here, kill it by using all the item in inventory (in order)
Hollow_Zone = Zone("Hollow Zone", "A cathedral of bone-white stone and shattered pews. Shadows ripple with unseen life. Here, Dark and Light Echoes may be joined into something new.", None, None) #Combine Dark Echo and Light Echo to form a new item
#IF YOU ALREADY HAD THE DARK ECHO YOU CAN SKIP ALL THESE ROOM
Dark_Zone = Zone("Dark Zone", "A black abyss of jagged stone where whispers crawl under your skin. The Dark Echo waits, feeding on fear and hesitation.", None, None) #Receive Dark Echo
Light_Zone = Zone("Light Zone", "A chamber of endless mirrored walls bathed in searing light. Every step exposes what hides within you, and the Light will burn away falsehoods.", None, None) #You use Light to UNlock the Secret Zone
Secret_Zone = Zone("Secret Zone", "A hidden sanctum of shifting corridors and looping halls. Solve the riddle that reshapes the room to earn the right to enter the Dark Zone.", None, None) # Solving Secret Zone To access Dark Zone

def randomStructure():
    Zones = [Choir_Fields, Echo_Zone,Hollow_Zone,Dark_Zone,Light_Zone,Secret_Zone] #Never take Safe Havens and Silent Zone
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

    for i in range(4):
        if i == 1: 
            RemainZone2.add_zone(Safe_Haven.linkedZone[0])
        elif i == 2:
            RemainZone2.add_zone(Silent_Zone)
        else:
            RemainZone2.add_zone(None) #Add none to the other direction
        
def direction(dir):
    if dir == 0:
        return "East"
    elif dir == 1:
        return "West"
    elif dir == 2:
        return "North"
    elif dir == 3:
        return "South"
    
def Safe_Haven_Function():
    print("Creatures can't cross the zone, I am safe here. At least I can easily accessed nearby Zone.")
    return

def Hollow_Choir_Function(): #Combine Echo
    print('"The shadow and light had balanced out the universe for a millenia, the formation create a strong power of lives that gives living to things."')
    if "Bright Echo" in player.inventory and "Dark Echo" in player.inventory:
        print("You can feel a strong power come from nowhere, the echoes keep vibrating non-stop, trying to speak up something.")
        #CODE HERE
    else:
        print("You are missing one of the sides...")
    return

def Light_Zone_Function():
    print('The room filled with light that shine through every sounds')
    print('You are holding it, you are holding the power')
    print('This is the beginning after the end')
    user_response = input('Would you like to use Bright Echo to unlock a hidden room?\n[1] Yes\n[2] No\n>>> ')
    if user_response == "1":
        print("The light absorbed the Echo. The zone started to rumble, wall collapsed and falling, bouncing back and one d-")
        print("You wake up in the debrises the Bright Echo is in your hand, trying to tell you something.")
    else:
        print("Are you sure about that? Don't worry you can comeback anytime when you are ready.")
    return

def Secret_Zone_Function():#Puzzle ADD A KEY TO MAKE SURE THAT PLAYER HAD ALREADY FINISHED LIGHT ZONE
    return

def Dark_Zone_Function():#Dialogue, reset map # A KEY
    return

def Echo_Zone_Function():#Collect echo minigame
    return

def Choir_Fields_Function():#Holy Bible
    return

def Silent_Zone_Function():
    return

    
randomStructure()

currentZone = Safe_Haven
while True:
    currentZone.inform_zone()
    for zoneDir in range(len(currentZone.linkedZone)):#Print direction guide
        if currentZone.linkedZone[zoneDir] is not None:
            print(f'"{currentZone.linkedZone[zoneDir].print_name()}" is at {direction(zoneDir)}') #Print in4

    userResponse = input('\n[1] East \n[2] West \n[3] North \n[4] South\n[5] Examine the area\n>>> ')
    if userResponse == "1":
        currentZone = currentZone.linkedZone[0]
    elif userResponse == "2":
        currentZone = currentZone.linkedZone[1]
    elif userResponse == "3":
        currentZone = currentZone.linkedZone[2]
    elif userResponse == "4":
        currentZone = currentZone.linkedZone[3]
    else:
        if currentZone == Safe_Haven:
            Safe_Haven_Function()
        elif currentZone == Hollow_Zone:
            Hollow_Choir_Function()
        elif currentZone == Light_Zone:
            Light_Zone_Function()
    time.sleep(2)
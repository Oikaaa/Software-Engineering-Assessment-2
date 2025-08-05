# I HAVE NO MOUTH, BUT I HAVE TO SCREAM
# Developed by: Jimmy (Huy Bao Thang)
# NOTE: PLEASE USE COMMON SENSE, DON'T TRY TO FIND BUGS
# Last Update: 3/8/2025
# Setting: 
# | Fifty years ago, the world was obliterated by The Soundfall — a resonance event of unknown origin. It ruptured memory, time, and sound itself. Survivors emerged unable to speak. Others became Hollowed, empty shells filled only with static.
# | What remains are scattered Echo Zones — warped places where memory loops and whispers invade the mind. Entering them is the only way to recover who you are — but doing so brings you closer to something else...
# | Something that remembers everything.
# Devlog:
# | 31/7/25: Started flesh, create prologue, player traits, locations and characters.
# | 2/8/25: Finish the first world (Marrowpoint Station) and event in it, with a few update to Location.py, Character.py (Add more function) and more dialogue.
# | 3/8/25: Completed The Flooded Bridge scenario gameplay, but not the dialogue
# | 4/8/25: Started working on Church of the Shattered Voice scenario in the test.py file, but there is still some bug in it. The gameplay will be try to remember the line and later on spot the different if there are any (Even user can just scroll up)
# | 5/8/25: Completed the scenario minigame; The game will show the line and you have to remember it, later on it will appear back randomly and you need to find the different.

# Modules
import time
import random
import os
from Classes.Characters import Character
from Classes.Characters import Enemy
from Classes.Characters import NPC
from Classes.Locations import Location
from Classes.Locations import Maze
from Dialogue import print_dialogue
player = Character(input('Your name is? '))

print('\n\n\n\n\n\n\n\n\n\n\n') #This one just for line break so player can see the text clearer
time.sleep(3)

# Prologue - This one is not in Dialogue.py is to show how the text printing works
print('') #Just for line break
print("-----I HAVE NO MOUTH, BUT I HAVE TO SCREAM-----")
print('')
time.sleep(8) #wait for 8 seconds
print(" | They say the world ended with a sound.")
time.sleep(5)
print(" | A sound so loud it tore through minds like glass through flesh.")
time.sleep(5)
print(" | Cities fell silent in an instant. Voices vanished.")
time.sleep(5)
print(" | Now, the sky hums with static, and the ground remembers too much.")
print('')
time.sleep(8)
print('You wake up alone in the ruins of a town once called Marrowpoint. The buildings are twisted, their steel frames grown like roots through the cracked streets. The sky above is a flickering sheet of red and black, as if reality is failing to load properly.')
time.sleep(6)
print("Your mouth is sealed.")
time.sleep(3)
print("Not with stitches.")
time.sleep(3)
print("Not with skin.")
time.sleep(5)
print("There’s simply… nothing where it used to be.")
time.sleep(5)
print("You try to scream. But in this world, there are no screams left. Only echoes.")
time.sleep(3)
print('')
time.sleep(3)
print('')
time.sleep(3)
print('')

# Main
print_dialogue("Introduction")

next_step = False #Check if it can move to next stage
while next_step is not True:
    trait = input("Choose one of the following items to interact (Choose wisely, they want to tell you something): ")
    print('')
    if trait == "1":#If they choose 1
        print('The forest behind them is warped — the trees are spiraled unnaturally, like soundwaves frozen in bark.')
        print('Words are carved into the photo’s surface:')
        print(' | “Don’t follow the singing. It’s not her.”')
        time.sleep(3)
        print('')
        player.set_trait("Wary")#Assign trait to character
        print('*** Trait gained: Wary *** \n You gain resistance to false memories.')
        print('')
        next_step = True#Next step

    elif trait == "2":#If they choose 2
        print('The tape hisses and skips. Then — a voice, distorted but familiar.')
        print('“ | ...if you’re hearing this, then I didn’t make it back.')
        print('  | Do not try to remember everything.')
        print('  | Some of it belongs to it now.”')
        time.sleep(3)
        print('')
        player.set_trait("Echo-Bound")
        print('*** Trait gained: Echo-Bound *** \n You can interact with corrupted audio terminals.')
        next_step = True

    elif trait == "3":#If they choose 3
        print('The world shifts. You’re no longer in the train station. You’re standing in ash, watching three burning figures walk into the sea. One turns to you — it has your eyes.')
        print('You jolt back to reality, but now you feel a presence watching you.')
        time.sleep(3)
        print('')
        player.set_trait("Fractured Memory")
        print('*** Trait gained: Fractured Memory *** \n Your dreams will be… wrong.')
        next_step = True

    else:#All other invalid input
        print("Please choose a valid value.")
        print('')

next_step = None
while next_step == None:
    next_step = input('[Enter to continue]')
print('')
#-------------
time.sleep(3)
print('Footsteps crunch outside the station. Something heavy. Dragging something metal.')
time.sleep(5)
print('You turn — there"s a figure in the doorway. A tall, ragged person with no mouth and too many eyes. They tilt their head.')
time.sleep(6)
print('They begin to hum.')
time.sleep(3)
print('')
time.sleep(3)
print('')
time.sleep(3)
print('')

#=========Marrowpoint=========
TheWather = Enemy('The Watcher', 'A tall, ragged figure who stands silently in the doorway, mouthless yet burdened with too many eyes that never blink.')
MarrowpointStation = Location('Marrowpoint Station', 'An abandoned, half-collapsed train station filled with dead electronics, scavenged shelters, and chalk warnings.', TheWather)
TheWather.add_weekness('Bright Echo')

time.sleep(3)
print(f"=========== {MarrowpointStation.name} =========== ")
print(f" | {MarrowpointStation.description}")
print(" | This place is ruled by the Watcher — a tall, ragged figure who stands silently in the doorway, mouthless yet burdened with too many eyes that never blink.")
print('')
print('/// OBJECTIVE: YOU NEED TO KILL THE WATCHER AND ACCESS ITS FRAGMENT ///')

next_step = False
while next_step is not True:
    time.sleep(3)
    print('')
    print('[1] Search the area \n[2] Fight the creature \n[3] Use your ability \n[4] Access inventory')
    print('')

    userResponse = input('>>> ')
    item = True #If the is something in the area
    if userResponse == "1":
        if item == True: #If there is something in the area
            print('You found a strong bright Echo on the ground.')
            time.sleep(2)
            print('Take it?')
            time.sleep(2)
            print('[1] Yes, pick it up \n[2] No, leave it on the ground')
            picking = input('>>> ')
            time.sleep(1)
            if picking == "1":
                print('You picked up the Echo, it can be use to burn the eyes.')
                player.add_inventory("Bright Echo")
                item == False #Player already picked up the item
            else:
                print('[...]')
        else:
            print("There is nothing in the area")
    elif userResponse == "2":
        print("You chose to fight the creature...")
        time.sleep(1)
        if len(player.inventory) == 0:#If there is no item
                print("YOU HAVE NOTHING TO USE")
        else:
            print("What items you want to use?")
            time.sleep(2)
            for item in range(len(player.inventory)):#Print all the items
                print(f"[{item + 1}] {player.inventory[item]}")
            choosing_weapon = input('>>> ')#Choose weapon
            try:
                if player.inventory[int(choosing_weapon) - 1] == TheWather.weekness:#-1 cuz player input range from 1 to n times, but the array of items start at 0
                    print("Creature dies from the brilliant light beam came from the shards, it burnt all the eyes on it head, left only dark blood came from the empty skull...")
                    time.sleep(3)
                    print('It died in pain, but made no sound, no scream at all...')
                    time.sleep(3)
                    print('A fragments came from it body...')
                    time.sleep(3)
                    print('As you carefully pick it up, a strong force pull you over...')
                    time.sleep(3)
                    print("[YOU'VE OBTAINED THE FRAGMENTS OF SIGHT]")
                    time.sleep(3)
                    print(' * You can now see for hint, but can only use it once per scenario...')
                else:
                    print("You failed to kill the creature... it ripped you in half, eat every flesh left on your body...")
                    time.sleep(5)
                    print("But your echo is still echoing around...")
                    time.sleep(3)
                    print('You came back from the death...')
                    time.sleep(3)
                    print('But this time... Play safe...')
            except:
                 print("You chose something that is not existed")
    elif userResponse == "3":
        time.sleep(1)
        print("You tried, but you can't")
    elif userResponse == "4":
        time.sleep(1)
        print('You acessed the inventory.')
        time.sleep(1)
        if len(player.inventory) == 0:#If there is no item
                print("There is nothing in your inventory.")
        else:
            for item in range(len(player.inventory)):#Print all the items
                    print(f" | [{item + 1}] {player.inventory[item]}")

next_step = None
while next_step == None:
    next_step = input('[Enter to continue]')

#=========The Flooded Bridge=========
#If sound happens before the cause, go to the opposite way of it; if sound happens after the cause, follow the sound
Ullin = NPC('Ullin', 'A rusted autonomous "Echo Crawler" bot who guides lost survivors through dangerous zones.')
TheFloodedHighway = Location('The Flooded Highway', 'A sunken stretch of freeway where sound warps — echoes arrive before the noise, twisting reality. Hazardous audio illusions lure the unwary into the depths. Ullin, the crawler bot, haunts these drowned roads.', Ullin)

Ullin.add_dialogue('—–zzzzKHT—voiceprint not—ACKNOWLEDGED.')
Ullin.add_dialogue('…wait. You. You’re... familiar. File not found. Still. You’re...you’re back.')
Ullin.add_dialogue('Are you—Are you the one who forgot?')
Ullin.add_dialogue('Or the one who lied?')
Ullin.add_dialogue('…Doesn’t matter. You’re all echoes in the end.')

#-----------------------------------------
#Dialogue here, another scenario stuuf
print_dialogue("The Flooded Bridge")

Room_1 = Maze("      ||   N   ||      \n" \
              "      ||       ||      \n" \
              "======||       ||======\n" \
              "                       \n" \
              "  W                 E  \n" \
              "======||       ||======\n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "         BEGIN          ", "A sound came from the west.")

Room_1_N = Maze("||=================||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||    ||     ||    ||\n" \
                "||    ||  S  ||    ||\n" \
                "||=====       =====||" , "Nothing's here.")

Room_1_W = Maze("||=================||      \n" \
                "||            []   ||      \n" \
                "||  .              ||======\n" \
                "||        O                \n" \
                "||            /         E  \n" \
                "||                 ||======\n" \
                "||    X            ||      \n" \
                "||                 ||      \n" \
                "||=================||" , "A box started to drop, but it create no sound.")

Room_2 = Maze("||=================||\n" \
              "                     \n" \
              " W                E  \n" \
              "||====||     ||====||\n" \
              "      ||     ||      \n" \
              "      ||     ||      \n" \
              "      ||     ||      \n" \
              "      ||  S  ||      \n" \
              "||=====       =====||" , "From east, you can see a giant rock felt into the river, it makes a huge splash sound.")

Room_2_S = Maze("||=====       =====||\n" \
                "||    ||  N  ||    ||\n" \
                "||    ||     ||    ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||                 ||\n" \
                "||=================||" , "Nothing's here.")

Room_3 = Maze("      ||   N   ||      \n" \
              "      ||       ||      \n" \
              "======||       ||======\n" \
              "                       \n" \
              "  W                 E  \n" \
              "======||       ||======\n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "           S          ", "From the darkness, a hum sound came from the North inside the deep tunnel.")

Room_3_S1 = Maze("      ||   N   ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||        \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||   S   ||     ", "You cant see anything, but darkness")

Room_3_S2 = Maze("      ||   N   ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||        \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||       ||      \n" \
                 "      ||   S   ||     ", "Something keeps humming, but you don't know what...")

Room_3_S3 = Maze("||=====       =====||\n" \
                 "||    ||  N  ||    ||\n" \
                 "||    ||     ||    ||\n" \
                 "||                 ||\n" \
                 "||                 ||\n" \
                 "||                 ||\n" \
                 "||                 ||\n" \
                 "||                 ||\n" \
                 "||=================||" , "The room is filled with pure darkness... You can't see your hand infront of you...")

Room_3_E = Maze("      ||=================||\n" \
                "      ||                 ||\n" \
                "======||                 ||\n" \
                "                         ||\n" \
                " W                       ||\n" \
                "======||                 ||\n" \
                "      ||                 ||\n" \
                "      ||                 ||\n" \
                "      ||=================||" , "A box started to drop, but it create no sound.")

Room_1.add_link(Room_2)#East
Room_1.add_link(Room_1_W)#West
Room_1.add_link(Room_1_N)#North
Room_1.add_link(None)#South

Room_1_W.add_link(Room_1)#
Room_1_W.add_link(None)#
Room_1_W.add_link(None)#
Room_1_W.add_link(None)#

Room_1_N.add_link(None)#
Room_1_N.add_link(None)#
Room_1_N.add_link(None)#
Room_1_N.add_link(Room_1)#

Room_2.add_link(Room_3)#
Room_2.add_link(Room_1)#
Room_2.add_link(None)#
Room_2.add_link(Room_2_S)#

Room_1_W.add_link(None)#
Room_1_W.add_link(None)#
Room_1_W.add_link(Room_2)#
Room_1_W.add_link(None)#

Room_3.add_link(Room_3_E)
Room_3.add_link(Room_2)#
Room_3.add_link("Room_3_N")
Room_3.add_link(Room_3_S1)

Room_3_E.add_link(None)#
Room_3_E.add_link(Room_3)#
Room_3_E.add_link(None)#
Room_3_E.add_link(None)#

Room_3_S1.add_link(None)#
Room_3_S1.add_link(None)#
Room_3_S1.add_link(Room_3)#
Room_3_S1.add_link(Room_3_S2)#

Room_3_S2.add_link(None)#
Room_3_S2.add_link(None)#
Room_3_S2.add_link(Room_3_S1)#
Room_3_S2.add_link(Room_3_S3)#

Room_3_S3.add_link(None)#
Room_3_S3.add_link(None)#
Room_3_S3.add_link(Room_3_S2)#
Room_3_S3.add_link(None)#

current_room = Room_1

#------Functions----------
def BugRoom(room):#When player try to hit the wall
    if room == None:
        print('"Why are you try to hit the wall?"\n\n\n')
        time.sleep(2)
        return previous_room
    return room

def NextStep(room):#If they are in the right room
    if room == "Room_3_N":
        return True
    return False

def TrickRoom(room):#If they are in the trick room
    if room == Room_3_S3:
        print("Use flashlight?\n[1] Yes\n[2] No")
        userIn = input(">>> ")
        if userIn == "1":
            return print("The room was lit up by the strong light source emited from the shards... but you just find an old computer that make a delay sound.")
        else:
            return print("...")
#------------------------

while NextStep(current_room) is False:
    print("")
    current_room.printMap()#Print the Map
    current_room.printDes()#Print the Description
    TrickRoom(current_room)

    print('[Ullin] Where do you want to go?\n[1] East\n[2] West\n[3] North\n[4] South')

    direction = input(">>> ")
    time.sleep(1)
    if direction == "1": #East
        previous_room = current_room
        current_room = current_room.linked_rooms[int(direction) - 1]#Current room became the room they chose to get in
        current_room = BugRoom(current_room)# This one jsut in case player try to get into a nonexist room, like a wall or sth
        NextStep(current_room)#To check are they in they winning room
    elif direction == "2": #West
        previous_room = current_room
        current_room = current_room.linked_rooms[int(direction) - 1]
        current_room = BugRoom(current_room)# This one jsut in case player try to get into a nonexist room, like a wall or sth
        NextStep(current_room)
    elif direction == "3": #North
        previous_room = current_room
        current_room = current_room.linked_rooms[int(direction) - 1]
        current_room = BugRoom(current_room)# This one jsut in case player try to get into a nonexist room, like a wall or sth
        NextStep(current_room)
    elif direction == "4": #South
        previous_room = current_room
        current_room = current_room.linked_rooms[int(direction) - 1]
        current_room = BugRoom(current_room)# This one jsut in case player try to get into a nonexist room, like a wall or sth
        NextStep(current_room)
    else:
        print("[Ullin] I don't think that's a way.")#They enter a random input

#Dialogue here, then move up to next scenario

#=========Church of the Shattered Voice=========

#Dialogue here

#Try to remember the hymms, if it appear for the first time, it's always right, if it's appear a second time, it might changed, and you need to find is it right or not
hymns = {
    "True_Hymn":{
        1: "In breathless dark, we knelt as one,",
        2: "The mouthless void, the rising sun,",
        3: "We sang in cords the world unspun,",
        4: "And bled our names into the drum.",
        5: "Echo, Echo, take my tongue,",
        6: "Carry silence where I’m from.",
        7: "Fold my voice in shattered glass,",
        8: "Let the final choir pass.",
        9: "A thousand throats, but none to cry,",
        10: "The bell fell dead, the heavens dry.",
        11: "We heard the hymn before the lie,",
        12: "The bell fell dead, the heavens dry.",
        13: "And swallowed truth in lullaby.",
        14: "I—am—not—the—mouth—I—spoke.",
        15: "Burn—the—song—and—keep—the—smoke.",
        16: "All who listened, all who knew,",
        17: "Now forget the voice was you.",      
    },
    "False_Hymn":{
        1: {
            1: "In breathless dark, you knelt as one,",
            2: "In holy dark, we knelt as one,",
            3: "In breathless dark, we knew as one,",
        },
        2: {
            1: "The mouthless void, the rising son,",
            2: "The mouthless voice, the rising sun,",
            3: "The mouthless void, the shining sun,",
        },
        3: {
            1: "We sang in chords the world unspun,",
            2: "We sang in cords the words unspun,",
            3: "We sang in cords as the world spin,",
        },
        4: {
            1: "And bleed our names into the drum.",
            2: "And bled our shames into the drum.",
            3: "And bled our names into the hums.",
        },
        5: {
            1: "Echo, Echo, take my soul,",
            2: "Echo, Echo, shake my tongue,",
            3: "Echo, Echo, shattered my tongue,",
        },
        6: {
            1: "Carry silence here I come.",
            2: "Lonely silence, where I’m from.",
            3: "Carry silence from my home.",
        },
        7: {
            1: "Fold my voice in shadowed cast,",
            2: "Hold my voice in shattered glass,",
            3: "Fold my soil in shattered glass,",
        },
        8: {
            1: "Let the final choice pass.",
            2: "Let the final echo pass.",
            3: "Let the final voice pass.",
        },
        9: {
            1: "A thousand throats, but none to die,",
            2: "A thousand throats, but none to cry,",
            3: "A thousand throats, but one to cry,",
        },
        10: {
            1: "The bell fell dead, the heavens cry.",
            2: "The bell fell dead, the heavens tried.",
            3: "The bell fell dead, the hell dry.",
        },
        11: {
            1: "We heard the hymn before the line,",
            2: "We heard the hymn before the sun,",
            3: "We heard the hymn after the lie,",
        },
        12: {
            1: "The bell fell dead, the heavens cry.",
            2: "The bell fell dead, the heavens tried.",
            3: "The bell fell dead, the hell dry.",
        },
        13: {
            1: "And swallowed night in lullaby.",
            2: "And swallowed voice in lullaby.",
            3: "And swallowed choir in lullaby.",
        },
        14: {
            1: "I—am—the—mouth—I—spoke.",
            2: "I—am—not—the—mouth—that-spoke.",
            3: "I—am—not—the—mouth—I—joke.",
        },
        15: {
            1: "Burn—the—song—and—feel—the—smoke.",
            2: "Burn—the—voice—and—keep—the—smoke.",
            3: "Burn—the—mouth—and—keep—the—smoke.",
        },
        16: {
            1: "All who prayed, all who knew,",
            2: "All who baptised, all who knew,",
            3: "All who listened, all who knelt,",
        },
        17: {
            1: "Now forget the voice was your.",
            2: "Now forget the song was you.",
            3: "Now forget the mouth was you.",
        },
    },
}


selected_hymns = [] # Empty list
while len(selected_hymns) < 6: # While the selected random hymns is less than 6, keep doing it
    random_number = random.randint(1,17) # Generate a random number from 1 to 17
    if random_number not in selected_hymns: # If that number (hymn) is not in the list yet, 
        selected_hymns.append(random_number) # Add it
    # If there is, skip it. Keep doing until there are 6 unique elements in the list

#FUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONS
def false_hymn_picker(hymn_id):
    if random.randint(0,1) == 1: # You will have to do the quiz
        TrueOrFalse = "1" # Value will only be 1 or 2 in string format
        if random.randint(0,1) == 1: # If they lost the gambling (random 5050 == 1), then they have to find the wrong one
            random_false_hymn = random.randint(1,3)
            print(f'\n"{hymns["False_Hymn"][hymn_id][random_false_hymn]}"') # Print the false hymn
            print("\nI had seen this one before, didn't I?") # Print the text
            TrueOrFalse = "2" # Set variable to 2
        else: # Lucky enough
            TrueOrFalse = "1" # Set variable to 1
            print(f'\n"{hymns['True_Hymn'][hymn_id]}"')# Print the right hymn

        user5050 = input("[1] The hymn is all correct\n[2] There is something wrong with the hymn\n>>> ")#Print the input text
        if user5050 == TrueOrFalse: # If the answer is correct
            return "Correct"
        else: # If the answer is wrong
            return "Wrong"
    else:
        #Do nothing
        return False # No gamble
    
def hymn_display(hymns_list, counter):
    hymn = hymns["True_Hymn"][hymns_list[counter]] # Select the correct hymn from the dictionary
    print(f'\n"{hymn}"') # Display the hymn
    input("[Enter to continue]")
    clearOutput()
    return hymns_list[counter] # return the id

def clearOutput():
    os.system('cls' if os.name == "nt" else 'clear')
#FUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONS

counter = 0
displayed_hymn = []
while counter < 6:
    hymn_id = hymn_display(selected_hymns, counter)
    displayed_hymn.append(hymn_id) # Add the hymn id that just displayed before
    picker_function_result = false_hymn_picker(displayed_hymn[0]) # Take the first id in the list

    clearOutput()

    if picker_function_result is not False: # THe function return something else (They played the minigame)
        if picker_function_result == "Correct":
            displayed_hymn.remove(displayed_hymn[0])
            clearOutput()
            print("It was right...I guessed")
        else:
            clearOutput()
            print("I don't think it's the answer...")
    else: # The function returned false, meaning that the player dont have to play this round
        print("[...] \n")

    counter += 1

while len(displayed_hymn) > 0: # Final check for all remain challenge, if there is
    hymn_id = displayed_hymn[0]
    picker_function_result = false_hymn_picker(hymn_id)

    if picker_function_result is not False:
        if picker_function_result == "Correct":
            displayed_hymn.remove(hymn_id)
            clearOutput()
            print("It is normal...")
        else:
            clearOutput()
            print("I don't think it's the answer...")
            clearOutput()

#Dialogue here, then move up to next scenario'

next_step = None
while next_step == None:
    next_step = input('[Enter to continue]')

#=========The Hollow Choir Zone=========

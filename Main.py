# I HAVE NO MOUTH, BUT I HAVE TO SCREAM
# Developed by: Jimmy (Huy Bao Thang)
# NOTE: PLEASE USE COMMON SENSE, DON'T TRY TO FIND BUGS
# Last Update: 5/8/2025
# Github source code: https://github.com/Oikaaa/Software-Engineering-Assessment-2/tree/main
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
# | 7/8/25: Added more dialogue and player can now use their ability that they got in first scenario in some cases.
# | 11/8/25: Make more function for some class, ultilize and minimize the repetition of some function
# | 13/8/25: Designing last scenario, added Zone class, random map structured created and player movement throught the zones.
# | 16/8/25: Add function for first 3 Zones

# Modules
import time
import random
import os
from Classes.Characters import Character
from Classes.Characters import Enemy
from Classes.Characters import NPC
from Classes.Locations import Location
from Classes.Locations import Maze
from Classes.Locations import Zone
from Dialogue import print_dialogue
player = Character(input('Your name is? '))

print('\n\n') #This one just for line break so player can see the text clearer
time.sleep(3)

# Prologue - This one is not in Dialogue.py is to show how the text printing works
print('') #Just for line break
print("-----I HAVE NO MOUTH, BUT I HAVE TO SCREAM-----")
print('')
time.sleep(5) #wait for 8 seconds
print(" | They say the world ended with a sound.")
time.sleep(3)
print(" | A sound so loud it tore through minds like glass through flesh.")
time.sleep(3)
print(" | Cities fell silent in an instant. Voices vanished.")
time.sleep(3)
print(" | Now, the sky hums with static, and the ground remembers too much.")
print('')
time.sleep(5)
print('You wake up alone in the ruins of a town once called Marrowpoint. The buildings are twisted, their steel frames grown like roots through the cracked streets. The sky above is a flickering sheet of red and black, as if reality is failing to load properly.')
time.sleep(4)
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
TheWather.add_weekness('Bright Echo')
MarrowpointStation = Location('Marrowpoint Station', 'An abandoned, half-collapsed train station filled with dead electronics, scavenged shelters, and chalk warnings.', 'This place is ruled by the Watcher — a tall, ragged figure who stands silently in the doorway, mouthless yet burdened with too many eyes that never blink.', "YOU NEED TO KILL THE WATCHER AND ACCESS ITS FRAGMENT")
MarrowpointStation.add_character(TheWather)

time.sleep(3)
MarrowpointStation.inform_scenario()

item = True #If the is something in the area
next_step = False
while next_step is not True:
    time.sleep(3)
    print('')
    print('[1] Search the area \n[2] Fight the creature \n[3] Use your ability \n[4] Access inventory')
    print('')

    userResponse = input('>>> ')
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
                    player.add_fragment("Fragment Of Sight")
                    time.sleep(3)
                    print(' * You can now see for hint, but can only use it once per scenario...')
                    next_step = True
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
TheFloodedHighway = Location('The Flooded Highway', 'A sunken stretch of freeway where sound warps — echoes arrive before the noise, twisting reality. Hazardous audio illusions lure the unwary into the depths. Ullin, the crawler bot, haunts these drowned roads.', 'A secret zone inside the bridge, where sound and effect are disturbed. The key to survive is, try to look for the cause, not the effect.', "YOU NEED TO ESCAPE THE MAZE AND OBTAIN THE FRAGMENT")
TheFloodedHighway.add_character(Ullin)

Ullin.add_dialogue('—–zzzzKHT—voiceprint not—ACKNOWLEDGED.')
Ullin.add_dialogue('…wait. You. You’re... familiar. File not found. Still. You’re...you’re back.')
Ullin.add_dialogue('Are you—Are you the one who forgot?')
Ullin.add_dialogue('Or the one who lied?')
Ullin.add_dialogue('…Doesn’t matter. You’re all echoes in the end.')

Ullin.add_dialogue("[Ullin] Then you're lighter than most, memory is ballast here.")#6
Ullin.add_dialogue("[Ullin] Too much, and you sink.")#7

Ullin.add_dialogue("[Ullin] They tried to dam the sound. It didn't work.")#8
Ullin.add_dialogue("[Ullin] Now the water remembers everything. It reflects more than faces.")#9

Ullin.add_dialogue("[Ullin] No. You walk. I listen.")#10
Ullin.add_dialogue("[Ullin] You'll know the bridge by what it refuses to carry.")#11

#-----------------------------------------
#Dialogue here, another scenario stuuf
print_dialogue("The Flooded Bridge")

Ullin.print_dialogue(random.randint(0,4))

print_dialogue("The Flooded Bridge Ullin")

user_input = input("[1] I don't remember anything.\n[2] Why is it flooded?\n[3] Lead the way.")

if user_input == "1":
    Ullin.print_dialogue(6)
    time.sleep(2)
    Ullin.print_dialogue(7)
elif user_input == "2":
    Ullin.print_dialogue(8)
    time.sleep(2)
    Ullin.print_dialogue(9)
elif user_input == "3":
    Ullin.print_dialogue(10)
    time.sleep(2)
    Ullin.print_dialogue(11)
else:
    print("...")

print_dialogue("The Flooded Bridge Narration")

Room_1 = Maze("      ||   N   ||      \n" \
              "      ||       ||      \n" \
              "======||       ||======\n" \
              "                       \n" \
              "  W                 E  \n" \
              "======||       ||======\n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "      ||       ||      \n" \
              "         BEGIN          ", "A sound came from the west.") #Room design

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

Room_2_S.add_link(None)#
Room_2_S.add_link(None)#
Room_2_S.add_link(Room_2)#
Room_2_S.add_link(None)#

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

TheFloodedHighway.inform_scenario()

#------Functions----------
def BugRoom(room):#When player try to hit the wall
    if room == None:
        print('"Why are you try to hit the wall?"\n\n\n')
        time.sleep(2)
        return previous_room
    return room

def NextStep(room):#If they are in the right room
    if room == "Room_3_N":
        print("You've found the right one... No thing is there, but a bright orb keep calling your name.")
        time.sleep(1)
        print("You slowly walk towards it, touch it with your own hand")
        time.sleep(2)
        print("[YOU'VE OBTAINED THE FRAGMENT OF MIND]")
        player.add_fragment("Fragment Of Mind")
        return True
    return False

Tricked_room_item = True
def TrickRoom(room):#If they are in the trick room
    if room == Room_3_S3:
        print("Use flashlight?\n[1] Yes\n[2] No")
        userIn = input(">>> ")
        if userIn == "1":
            #Found soemthing
            if Tricked_room_item == True:
                print('You found a strong Dark Echo on the ground.')
                time.sleep(2)
                print('Take it?')
                time.sleep(2)
                picking = input('[1] Yes, pick it up \n[2] No, leave it on the ground\n>>> ')
                time.sleep(1)
                if picking == "1":
                    print('You picked up the Echo, it swallow the darkness around it.')
                    player.add_inventory("Dark Echo")
                    Tricked_room_item == False #Player already picked up the item
                else:
                    print('[...]')
                return False
            else:
                return print("The room was lit up by the strong light source emited from the shards... but you just find an old computer that make a delay sound.")
        else:
            return print("[...]")
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

#=========Church of the Shattered Voice=========
Seren = NPC("Seren", "A mouthless nun of hymns.")
TheChurchOfTheShatteredVoice = Location("The Church of the Shattered Voice", "A church where lost soul stay, only the soud of truth can pass. This is also home of Seren, a nun of hymns.", "A home to many lost soul who passed without a sound, there is a nun who will testify the purity of echo through hymns. She will sing a poety. First time appear always true, second time can wrong...", "Complete Seren Challenge")

Seren.add_dialogue("[Seren] You get that wrong, but don't worry, you can try again.")
Seren.add_dialogue("[Seren] Your soul is on the eadge,...")
Seren.add_dialogue("[Seren] Try to memorize it...")
Seren.add_dialogue("[Seren] I don't think that is the right answer.")
Seren.add_dialogue("[Seren] One more try, no more, no less")

print_dialogue("The Church Prologue") #And epilogue for the previous ep

time.sleep(3)
TheChurchOfTheShatteredVoice.inform_scenario()
time.sleep(2)
counter = 0
if player.trait == "Wary":
    print("Your echo keep bumping, something is telling you, talking to you without a mouth.")
    time.sleep(2)
    print("[Your trait 'Wary' can have prevent false memory, which is powerful for this scenario, do you want to use ?]")
    time.sleep(2)
    user_input1 = input("[1] Yes (You will skip the scenario without playing it.)\n[2] No my memory is good enough to do this challenge.\n>>> ")
    if user_input1 == "1":
        counter = 6
    else:
        counter = 0

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

#FUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONS vvvv
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

def random_dialogue(character):
    return print(character.print_dialogue(random.randint(0,4)))
#FUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONS ^^^^

print("Try to remember the hymms, if it appear for the first time, it's always right, if it's appear a second time, it might changed, and you need to find is it right or not")
input("[Enter to continue]")

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
            random_dialogue(Seren)
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

print("[YOU'VE OBTAINED THE FRAGMENT OF SOUL]")
player.add_fragment("Fragment Of Soul")

next_step = None
while next_step == None:
    next_step = input('[Enter to continue]')

#Dialogue

#=========The Hollow Choir Zone=========
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
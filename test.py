from Classes.Locations import Location
from Classes.Characters import Character
from Classes.Characters import NPC
from Classes.Characters import Enemy
from Classes.Locations import Maze
import time
import os
import random
player = Character('Guest')

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
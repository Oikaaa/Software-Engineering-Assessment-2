import time
#It works the same as the first one you see in the main.py, but I decided to make a seperate file so that the main one won't be so messy with alot of dialogue
Dialogue = {
    "Introduction":{
        1:{
            "Text": "You awaken in the husk of an old train station. The walls pulse with faint light.",
            "Duration": 5
        },
        2:{
            "Text": "A crow lies dead beside you — its beak torn off. The air smells like static and rust.",
            "Duration": 5
        },
        3:{
            "Text": "A broken holographic kiosk blinks to life.",
            "Duration": 3
        },
        4:{
            "Text": " | WELCOME TO MARROWPOINT",
            "Duration": 3
        },
        5:{
            "Text": " | Population: --",
            "Duration": 3
        },
        6:{
            "Text": " | Voiceprint not found. Please registe-",
            "Duration": 2
        },
        7:{
            "Text": "The screen flickers, then dies.",
            "Duration": 0
        },
        8:{
            "Text": "",
            "Duration": 3
        },
        9:{
            "Text": " | You don’t remember who you are.",
            "Duration": 3
        },
        10:{
            "Text": " | You don’t know how long you’ve been here.",
            "Duration": 3
        },
        11:{
            "Text": " | But in your coat, you find three strange items:",
            "Duration": 3
        },
        12:{
            "Text": "",
            "Duration": 0
        },
        13:{
            "Text": "1. A cracked photo of a family standing in a mist-filled forest. The faces are scratched out.",
            "Duration": 0
        },
        14:{
            "Text": "2. A tape recorder — broken, but something’s inside.",
            "Duration": 0
        },
        15:{
            "Text": "3. A metal shard that hums when you hold it — like it wants to whisper something.",
            "Duration": 0
        },
        16:{
            "Text": "",
            "Duration": 0
        },
        17:{
            "Text": " | [1] Examine the photo\n | [2] Play the tape recorder\n | [3] Touch the metal shard to your forehead",
            "Duration": 0
        },
        17:{
            "Text": "",
            "Duration": 0
        },
    },
    "The Flooded Bridge":{
        1:{
            "Text": "The metal bones of Marrowpoint Station groan beneath your feet.",
            "Duration": 2
        },
        2:{
            "Text": "The wind does not whistle here. It chokes.",
            "Duration": 2
        },
        3:{
            "Text": "Faint speaker static crackles overhead — or is it whispering your name?",
            "Duration": 2
        },
        4:{
            "Text": "You found a robot lying on the ground...",
            "Duration": 0
        },
    },
    "The Flooded Bridge Ullin":{
        1:{
            "Text": "[...]",
            "Duration": 2
        },
        2:{
            "Text": "Good. You're breathing. Means you still count.",
            "Duration": 2
        },
        3:{
            "Text": "Echo count: Four remaining. Memory weight: unstable.",
            "Duration": 2
        },
        4:{
            "Text": "Next is The Flooded Bridge. You remember that?",
            "Duration": 2
        },
    },
    "The Flooded Bridge Narration":{
        1:{
            "Text": "The tunnel narrows, lit only by pulsing hazard lights that no longer mean anything.",
            "Duration": 2
        },
        2:{
            "Text": "A bent sign reads: 'CAUTION: SOUND LEVELS BEYOND THIS POINT MAY CAUSE VOMITING OR PRAYER.'",
            "Duration": 2
        },
        3:{
            "Text": "You and Ullin walked for 2 hours, through the debris, smoke, and fire.",
            "Duration": 5
        },
        4:{
            "Text": "You emerge into pale light.",
            "Duration": 2
        },
        5:{
            "Text": "The bridge yawns across a drowned city gorge. You are inside the bridge, where there is a maze with many rooms.",
            "Duration": 2
        },
        6:{
            "Text": "Its handrails are made of human voiceboxes — fossilized, lacquered.",
            "Duration": 2
        },
        7:{
            "Text": "Something weeps beneath the water, but the ripples never reach shore.",
            "Duration": 2
        },
        8:{
            "Text": "[Ullin] Careful. The bridge doesn’t like indecision.",
            "Duration": 2
        },
        9:{
            "Text": "[Ullin] Step too light, and it forgets you.",
            "Duration": 2
        },
        10:{
            "Text": "[Ullin ]Step too heavy, and it remembers someone else.",
            "Duration": 2
        },
        11:{
            "Text": "[Ullin] Remember, step to the event, not the sound",
            "Duration": 2
        },
        12:{
            "Text": "[Ullin] If something happens before the caused, go the opposite direction,",
            "Duration": 2
        },
        13:{
            "Text": "[Ullin] If if the caused happens before the effect, go straigth for it.",
            "Duration": 2
        },
    },
    "The Church Prologue":{
        1:{
            "Text": "The air dries as you leave the soaked planks behind.\nThe ground is jagged, gleaming with broken mirror-glass and petrified blood.\nThe Spire looms ahead — a cathedral made entirely of shattered reflective surfaces.\nNo door. Only the echo of footsteps you haven't taken yet.",
            "Duration": 5
        },
        2:{
            "Text": "Ullin perches nearby, crouched like a broken insect.",
            "Duration": 2
        },
        3:{
            "Text": "[YOU] What is this place?",
            "Duration": 2
        },
        4:{
            "Text": "[Ullin] Before the Collapse, they came here to be seen by something divine.\nNow, the Spire watches itself.\nIf you look too long, it may remember a version of you that never left.",
            "Duration": 4
        },
        5:{
            "Text": "[YOU] What do I do here?",
            "Duration": 2
        },
        6:{
            "Text": "[Ullin] Every Echo Zone demands a toll.\nHere, you must give up a truth. A real one.\nListen to the hymn. If it accepts, you pass.\nIf not... hope it reflects something kind.",
            "Duration": 2
        },
        7:{
            "Text": "Suddenly in the dark, a woman with a nun outfit came out",
            "Duration": 2
        },
        8:{
            "Text": "[Ullin] She is Seren, the only nun in this church who take the responsibility to testify the purity of your echo. She will sing and you have to guess is it true or wrong.",
            "Duration": 2
        },
        9:{
            "Text": "[Ullin] Only people with strong echo can be able to memorize all the hymn pattern, but some with a weak echo may not.",
            "Duration": 2
        },
        10:{
            "Text": "[You] So what should I do now?",
            "Duration": 2
        },
        11:{
            "Text": "[Seren] Just complete the challenge and I'll let you go, but if you fail, your echo will be trapped here forever.",
            "Duration": 2
        },
        12:{
            "Text": "[YOU] ...",
            "Duration": 2
        },
    }
}

def print_dialogue(current_scenario):#Printing dialogues function
    for dialogue in Dialogue[current_scenario]:#For each dialogue in the scenario of the "Dialogue" dictionary
        print(Dialogue[current_scenario][dialogue]["Text"])#print the first text from that scenario
        time.sleep(Dialogue[current_scenario][dialogue]["Duration"])#delay for the amount of duration after the text is printed
        #Then continue to print the next text from top to bottom, until there is no more text

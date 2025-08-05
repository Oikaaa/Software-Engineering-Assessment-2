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
            "Text": "Lorem",
            "Duration": 0
        },
    }
}

def print_dialogue(current_scenario):#Printing dialogues function
    for dialogue in Dialogue[current_scenario]:#For each dialogue in the scenario of the "Dialogue" dictionary
        print(Dialogue[current_scenario][dialogue]["Text"])#print the first text from that scenario
        time.sleep(Dialogue[current_scenario][dialogue]["Duration"])#delay for the amount of duration after the text is printed
        #Then continue to print the next text from top to bottom, until there is no more text

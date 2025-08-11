from Classes.Locations import Location
from Classes.Characters import Character
from Classes.Characters import NPC
from Classes.Characters import Enemy
from Classes.Locations import Maze
import time
import os
import random
player = Character('Guest')

# Please NOTE that don't let the character ABILITY WASTED AND INVENTORY (iykyk)
Ullin = NPC('Ullin', 'A rusted autonomous "Echo Crawler" bot who guides lost survivors through dangerous zones.')
TheFloodedHighway = Location('The Flooded Highway', 'A sunken stretch of freeway where sound warps — echoes arrive before the noise, twisting reality. Hazardous audio illusions lure the unwary into the depths. Ullin, the crawler bot, haunts these drowned roads.', 'A secret zone inside the bridge, where sound and effect are disturbed. The key to survive is, try to look for the cause, not the effect.', "YOU NEED TO ESCAPE THE MAZE AND OBTAIN THE FRAGMENT")
TheFloodedHighway.add_character(Ullin)

TheFloodedHighway.inform_scenario()
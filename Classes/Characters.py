class Character:
    def __init__(self, name):
        self.name = name
        self.trait = None
        self.inventory = []
        self.fragments = []

    def set_trait(self, trait):
        self.trait = trait # 3 available traits: Wary, Echo-Bound, Fractured Memory

    def add_inventory(self, item):
        self.inventory.append(item)

    def add_fragment(self, fragment):
        self.fragments.append(fragment)

class NPC(Character): # Son of Character
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.dialogue = []

    def add_dialogue(self, dialogue):
        self.dialogue.append(dialogue)

    def print_dialogue(self, number):
        print(self.dialogue[number])
    

class Enemy(Character): # 2nd Son of Character
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.weekness = None

    def add_weekness(self, weekness):
        self.weekness = weekness
class Character:
    def __init__(self, name):
        self.name = name
        self.trait = None
        self.inventory = []

    def set_trait(self, trait):
        self.trait = trait # 3 available traits: Wary, Echo-Bound, Fractured Memory

    def add_inventory(self, item):
        self.inventory.append(item)

class NPC(Character):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.dialogue = []

    def add_dialogue(self, dialogue):
        self.dialogue.append(dialogue)
    

class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.weekness = None

    def add_weekness(self, weekness):
        self.weekness = weekness
class Location:
    def __init__(self, name, descriprion, hint, objective):
        self.name = name
        self.description = descriprion
        self.hint = hint
        self.characters = []
        self.objective = objective

    def print_name(self):
        return print(self.name)
    
    def print_description(self):
        return print(self.description)
    
    def add_character(self, character):
        self.characters.append(character)


    def inform_scenario(self):
        print(f"=========== {self.name} =========== ")
        print(f" | {self.description}")
        print(f" | {self.hint}")
        print("Character:")
        for character in self.characters:
            print(f' | {character.name}, {character.description}')
        print('')
        print(f'/// OBJECTIVE: {self.objective} ///')
    

class Maze(Location):
    def __init__(self, map, description):
        super().__init__(None, description, None, None)
        self.map = map
        self.linked_rooms = []#North South, East, West
        self.items = None

    def add_link(self, room):
        self.linked_rooms.append(room)

    def printMap(self):
        return print(self.map)
    
    def printDes(self):
        return print(f'"{self.description}"\n')
    
    def add_item(self, item):
        self.items = item

class Zone(Location):
    def __init__(self, name, description, character, item):
        super().__init__(name, description, None, None)
        self.character = character
        self.item = item
        self.linkedZone = []

    def add_zone(self, zone):
        self.linkedZone.append(zone)

    def inform_zone(self):
        print(f"=========== {self.name} =========== ")
        print(self.description)

    def print_name(self):
        return self.name
class Location:
    def __init__(self, name, descriprion, character):
        self.name = name
        self.description = descriprion
        self.character = character
        pass

class Maze():
    def __init__(self, map, description):
        self.map = map
        self.description = description
        self.linked_rooms = []#North South, East, West

    def add_link(self, room):
        self.linked_rooms.append(room)

    def printMap(self):
        return print(self.map)
    
    def printDes(self):
        return print(f'"{self.description}"\n')
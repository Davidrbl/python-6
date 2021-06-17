class Room:
    def __init__(self, _name, _exits=[], _items=[], _people=[]):
        self.exits = _exits
        self.items = _items
        self.people = _people
        self.name = _name

    def add_exit(self, room):
        self.exits.append(room)

    def describe(self, game):
        game.printHeader()

        #Naam generaten
        game.printRegel("Je bent nu in: " + self.name)

        #Zeggen wat erin is
        game.printRegel(game.show_list(self.items, "Items in this room"))

        game.printRegel(game.show_list(self.people, "People in this room"))

        game.printRegel(game.show_list(self.exits, "Exits"))

        game.printFooter()

    def add_item(self, item):
        self.items.append(item)

    def add_person(self, person):
        self.people.append(person)

    def getExits(self):
        return self.exits

    def setExits(self, exits):
        self.exits = exits

    def getItems(self):
        return self.items

    def setItems(self, items):
        self.items = items

    def getPeople(self):
        return self.people

    def setPeople(self, people):
        self.people = people

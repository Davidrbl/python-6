from Room import Room
from Key import Key
from NPC import NPC
from Item import Item
from Triforce import Triforce

class World:
    def __init__(self, _rooms=[]):
        self.rooms = _rooms

    def create_world(self):
        '''Cave = Room("Cave")
        River = Room("River")
        Town = Room("Town")
        Forest = Room("Forest")
        Mountains = Room("Mountains")
        Castle = Room("Castle")
        Wizard_Lab = Room("Wizard's lab")

        #exitsstring='\n'
        #for i in self.rooms:
        #    exitsstring += i.name + "\n"
        #print("World rooms:" + exitsstring)

        #EXITS Cave
        Cave.exits.append(River)
        #Cave.add_exit(River) #NAAR RIVER
        #Cave.add_exit(Town) #NAAR TOWN
        #EXITS River
        #River.add_exit(Cave) #NAAR CAVE
        #River.add_exit(Forest) #NAAR FOREST
        #River.add_exit(Wizard_Lab) #NAAR WIZARD'S LAB
        #EXITS Town
        #Town.add_exit(Cave) #NAAR CAVE
        #Town.add_exit(Mountains) #NAAR MOUNTAINS
        #Town.add_exit(Wizard_Lab) #NAAR WIZARD'S LAB
        #EXITS Forest
        #Forest.add_exit(River) #NAAR RIVER
        #Forest.add_exit(Castle) #NAAR CASTLE
        #Forest.add_exit(Wizard_Lab) #NAAR WIZARD'S LAB
        #EXITS Mountains
        #Mountains.add_exit(Town) #NAAR TOWN
        #Mountains.add_exit(Castle) #NAAR CASTLE
        #Mountains.add_exit(Wizard_Lab) #NAAR WIZARD'S LAB
        #EXITS Castle
        #Castle.add_exit(Forest) #NAAR FOREST
        #Castle.add_exit(Mountains) #NAAR MOUNTAINS
        #EXITS Wizard's lab
        #Wizard_Lab.add_exit(River) #NAAR RIVER
        #Wizard_Lab.add_exit(Town) #NAAR TOWN
        #Wizard_Lab.add_exit(Forest) #NAAR FOREST
        #Wizard_Lab.add_exit(Mountains) #NAAR MOUNTAINS

        self.add_room(Cave)
        self.add_room(River)
        self.add_room(Town)
        self.add_room(Forest)
        self.add_room(Mountains)
        self.add_room(Castle)
        self.add_room(Wizard_Lab)
        '''
        #==========KEYS==========#

        key_casF = Key("Key to castle", [3, 4], [5], ["Key to castle"])
        key_casM = Key("Key to castle", [3, 4], [5], ["Key to castle"])

        key_labC = Key("Key to Laboratory", [1, 2, 3, 4], [6], [])

        #==========NPCS==========#
        Jan = NPC("Jan", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", Item("bla", []))

        #=======TRICFORCES=======#
        tf1 = Triforce("Triforce of the knights")
        tf2 = Triforce("Triforce of the woods")
        tf3 = Triforce("Triforce of the wizard")

        self.Cave = Room("Cave", [1, 2], [], [Jan])
        self.River = Room("River", [0, 3])
        self.Town = Room("Town", [0, 4])
        self.Forest = Room("Forest", [1], [key_casF, tf2])
        self.Mountains = Room("Mountains", [2], [key_casM])
        self.Castle = Room("Castle", [], [key_labC, tf1])
        self.Wizard_Lab = Room("Laboratory", [], [tf3])

        self.rooms = [self.Cave, self.River, self.Town, self.Forest, self.Mountains, self.Castle, self.Wizard_Lab]

        #Exits goed maken voor de rooms.
        for i in self.rooms:
           exitlist = []
           for j in i.exits:
              exitlist.append(self.rooms[j])
              i.exits = exitlist


    def add_room(self, room):
        self.rooms.append(room)

    def first_room(self):
        return self.rooms[0]

    def deleteItemsWithName(self, name):
        for room in self.rooms:
            itemindex = 0
            length = len(room.items)
            while (itemindex < length):
                if (room.items[itemindex].getName() == name):
                    room.items.pop(itemindex)
                    itemindex -= 1
                    length -= 1

                itemindex += 1

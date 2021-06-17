from Room import Room
from Key import Key
from NPC import NPC
from Item import Item
from Triforce import Triforce
from lxml import etree

class World:
    def __init__(self, _rooms=[]):
        self.rooms = _rooms

    def create_world(self):
        numrooms = 7
        #==========ITEMS=========#
        rock = Item("A rock", "Cave")
        test = Item("test", "River")

        allItems = [rock, test]
        #==========KEYS==========#
        key_casF = Key("Key to castle", "Forest", ["Forest", "Mountains"], ["Castle"], ["Key to castle"])
        key_casM = Key("Key to castle", "Mountains",["Forest", "Mountains"], ["Castle"], ["Key to castle"])

        key_labC = Key("Key to Laboratory", "Castle", ["River", "Town", "Forest", "Mountains"], ["Laboratory"], [])

        allkeys = [key_casF, key_casM, key_labC]
        #==========NPCS==========#
        Jan = NPC("The Old King", "Castle", "oi im the old king heres a bla", Item("bla", "Castle"))
        Fisherman = NPC("An old fisherman","River" ,"Hey, was that you, walkin' out that cave? Hmm... Not the talkative type I see. You don't look too good, there's a town nearby if you wanna clean yourself up a little bit. Out here, your're gonna need every bit of help you can get, and it's dangerous to go alone, so, take this.", Item("A disgusting fish", "River"))

        allnpcs = [Jan, Fisherman]
        #=======TRICFORCES=======#
        tf1 = Triforce("Triforce of the knights", "Castle")
        tf2 = Triforce("Triforce of the woods", "Forest")
        tf3 = Triforce("Triforce of the wizard", "Laboratory")

        alltriforces = [tf1, tf2, tf3]

        #=========ROOMNAMES=======#
        self.allnames = ["Cave", "River", "Town", "Forest", "Mountains", "Castle", "Laboratory"]

        #==========ROOMEXITS=======#
        allexits = [["River", "Town"],["Cave", "Forest"],["Cave", "Mountains"],["River"],["Town"],[],[]]

        #==========ROOMS==========#
        itemlist = []
        npclist = []

        for i in range(numrooms):
            itemlist.append([])
            npclist.append([])

        for item in allItems:
            #ITEMS GOEDMAKEN
            print("Item: " + item.getName() + " gaat naar " + self.allnames[self.allnames.index(item.getPlace())])
            itemlist[self.allnames.index(item.getPlace())].append(item)

        for key in allkeys:
            #KEYS GOEDMAKEN
            print("Item: " + key.getName() + " gaat naar " + self.allnames[self.allnames.index(key.getPlace())])
            itemlist[self.allnames.index(key.getPlace())].append(key)

        for npc in allnpcs:
            #NPCS GOEDMAKEN
            print("Item: " + npc.getName() + " gaat naar " + self.allnames[self.allnames.index(npc.getPlace())])
            npclist[self.allnames.index(npc.getPlace())].append(npc)

        for tri in alltriforces:
            #TRIFORCES GOEDMAKEN
            print("Item: " + tri.getName() + " gaat naar " + self.allnames[self.allnames.index(tri.getPlace())])
            itemlist[self.allnames.index(tri.getPlace())].append(tri)

        #Exits goed maken voor de rooms.

        self.rooms = []
        for i in range(numrooms):
            #print("Creating room with name: " + self.allnames[i] + " exits: " + str(allexits[i]) + " items: " + str(itemlist[i]) + " npcs: " + str(npclist[i]))
            newroom = Room(self.allnames[i], allexits[i], itemlist[i], npclist[i])
            self.rooms.append(newroom)


        for room in self.rooms:
            #EXITS GOEDMAKEN
            exitslist = []
            for exit in room.getExits():
                try:
                    exitslist.append(self.rooms[self.allnames.index(exit)])
                except Exception as err:
                    print('ERROR bij syncing van rooms en exits' + str(err))
            room.setExits(exitslist)

    def create_worldXML(self, location):
        tree = etree.parse(location)

        root = tree.getroot()

        self.rooms = []
        self.numrooms = 0
        self.allnames = []

        for room in root.findall("Room"):
            roomname = room.attrib["name"]
            self.allnames.append(roomname)
            self.numrooms += 1

            roomexits = []
            for exit in room.findall("Exit"):
                print(exit.attrib)
                roomexits.append(exit.attrib["name"])

            roomitems = []
            for item in room.findall("Item"):
                print(item.attrib)
                itemname = item.attrib["name"]
                itemdupes = item.attrib["dupes"]
                if (itemdupes == ''):
                    itemdupes = []
                else:
                    itemdupes = itemdupes.split(',')
                itemobject = Item(itemname, "", itemdupes)
                roomitems.append(itemobject)

            roomnpcs = []
            for npc in room.findall("NPC"):
                print(npc.attrib)
                hasitem = False
                npcname = npc.attrib["name"]
                npcdialogue = npc.text
                if (len(npc.findall("Item")) is not 0):
                    hasitem = True
                    npcitem = npc.find("Item")
                    npcitemname = npcitem.attrib["name"]
                    npcitemdupes = npcitem.attrib["dupes"].split(",")
                    npcitem = Item(npcitemname, "", npcitemdupes)

                if hasitem:
                    npcobject = NPC(npcname, "", npcdialogue, npcitem)
                else:
                    npcobject = NPC(npcname, "", npcdialogue)

                roomnpcs.append(npcobject)

            roomobject = Room(roomname, roomexits, roomitems, roomnpcs)
            self.rooms.append(roomobject)

        print('epic poggers')
        print(self.numrooms)

        for room in self.rooms:
            #EXITS GOEDMAKEN
            exitslist = []
            for exit in room.getExits():
                #try:
                exitslist.append(self.rooms[self.allnames.index(exit)])
                #except Exception as err:
                #    print('ERROR bij syncing van rooms en exits' + str(err))
            room.setExits(exitslist)

    def create_worldTXT(self, location):
        #========GETELEMENTS++++++#

        #==========ROOMS==========#
        itemlist = []
        npclist = []

        for i in range(numrooms):
            itemlist.append([])
            npclist.append([])

        for item in allItems:
            #ITEMS GOEDMAKEN
            print("Item: " + item.getName() + " gaat naar " + self.allnames[self.allnames.index(item.getPlace())])
            itemlist[self.allnames.index(item.getPlace())].append(item)

        for key in allkeys:
            #KEYS GOEDMAKEN
            print("Item: " + key.getName() + " gaat naar " + self.allnames[self.allnames.index(key.getPlace())])
            itemlist[self.allnames.index(key.getPlace())].append(key)

        for npc in allnpcs:
            #NPCS GOEDMAKEN
            print("Item: " + npc.getName() + " gaat naar " + self.allnames[self.allnames.index(npc.getPlace())])
            npclist[self.allnames.index(npc.getPlace())].append(npc)

        for tri in alltriforces:
            #TRIFORCES GOEDMAKEN
            print("Item: " + tri.getName() + " gaat naar " + self.allnames[self.allnames.index(tri.getPlace())])
            itemlist[self.allnames.index(tri.getPlace())].append(tri)

        #Exits goed maken voor de rooms.

        self.rooms = []
        for i in range(numrooms):
            #print("Creating room with name: " + self.allnames[i] + " exits: " + str(allexits[i]) + " items: " + str(itemlist[i]) + " npcs: " + str(npclist[i]))
            newroom = Room(self.allnames[i], allexits[i], itemlist[i], npclist[i])
            self.rooms.append(newroom)


        for room in self.rooms:
            #EXITS GOEDMAKEN
            exitslist = []
            for exit in room.getExits():
                try:
                    exitslist.append(self.rooms[self.allnames.index(exit)])
                except Exception as err:
                    print('ERROR bij syncing van rooms en exits' + str(err))
            room.setExits(exitslist)

    def add_room(self, room):
        self.rooms.append(room)

    def first_room(self):
        return self.rooms[0]

    def deleteItemsWithName(self, name):
        for room in self.rooms:
            itemindex = 0
            length = len(room.items)
            while (itemindex < length):
                print("checking " + room.items[itemindex].name + " == " + name)
                if (room.items[itemindex].getName() == name):
                    room.items.pop(itemindex)
                    itemindex -= 1
                    length -= 1

                itemindex += 1

    def addExitsTo(self, rooms1, rooms2):
        roomsindex1 = []
        for i in rooms1:
            roomsindex1.append(int(self.allnames.index(i)))

        roomsindex2 = []
        for i in rooms2:
            roomsindex2.append(int(self.allnames.index(i)))


        for i in roomsindex1:
            for j in roomsindex2:
                self.rooms[i].add_exit(self.rooms[j])
                self.rooms[j].add_exit(self.rooms[i])

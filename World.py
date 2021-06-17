from Room import Room
from Key import Key
from NPC import NPC
from Item import Item
from Triforce import Triforce
from lxml import etree

class World:
    def __init__(self, _rooms=[]):
        self.rooms = _rooms

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
                roomexits.append(exit.attrib["name"])

            roomitems = []
            for item in room.findall("Item"):
                itemname = item.attrib["name"]
                itemdupes = item.attrib["dupes"]
                if (itemdupes == ''):
                    itemdupes = []
                else:
                    itemdupes = itemdupes.split(',')
                itemobject = Item(itemname, itemdupes)
                roomitems.append(itemobject)

            for key in room.findall("Key"):
                keyname = key.attrib["name"]
                keydupes = key.attrib["dupes"]
                if (keydupes == ''):
                    keydupes = []
                else:
                    keydupes = keydupes.split(',')
                keyrooms1 = key.attrib["rooms1"].split(",")
                keyrooms2 = key.attrib["rooms2"].split(",")
                keyobject = Key(keyname, keyrooms1, keyrooms2, keydupes)
                roomitems.append(keyobject)

            for tri in room.findall("Tri"):
                triname = tri.attrib["name"]
                triobject = Triforce(triname)
                roomitems.append(triobject)

            roomnpcs = []
            for npc in room.findall("NPC"):
                hasitem = False
                npcname = npc.attrib["name"]
                npcdialogue = npc.text
                if (len(npc.findall("Item")) is not 0):
                    hasitem = True
                    npcitem = npc.find("Item")
                    npcitemname = npcitem.attrib["name"]
                    npcitemdupes = npcitem.attrib["dupes"]
                    if (npcitemdupes == ''):
                        npcitemdupes = []
                    else:
                        npcitemdupes = npcitemdupes.split(',')
                    npcitem = Item(npcitemname, npcitemdupes)

                if hasitem:
                    npcobject = NPC(npcname, npcdialogue, npcitem)
                else:
                    npcobject = NPC(npcname, npcdialogue)

                roomnpcs.append(npcobject)

            roomobject = Room(roomname, roomexits, roomitems, roomnpcs)
            self.rooms.append(roomobject)

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

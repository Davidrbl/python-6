class Player:
    def __init__(self, _name, _inventory=[], _location=None):
        self.name = _name
        self.inventory = _inventory
        self.location = _location

    def goto_room(self, roomname):
        for i in self.location.exits:
            if (i.name == roomname):
                self.set_current_room(i)
                break

    def set_current_room(self, room):
        self.location = room

    def get_current_room(self):
        return self.location

    def pick_up(self, itemstring, room, game):
        for i in range(len(room.items)):
            if (room.items[i].name == itemstring):
                item = room.items[i]
                self.inventory.append(item)
                room.items[i].onPickup(game)
                #room.items.pop(i)
                break

    def talkTo(self, name, game):
        for i in self.location.getPeople():
            if (i.getName() == name):
                i.onTalk(game)
                break

    def getInventory(self):
        return self.inventory

    def setInventory(self, inventory):
        self.inventory = inventory

    def getName(self):
        return self.name

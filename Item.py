class Item:
    def __init__(self, _name, _place, dupes=[]):
        self.name = _name
        self.place = _place
        self.dupes = dupes

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPlace(self):
        return self.place

    def onPickup(self, game):
        if (len(self.dupes) != 0):
            for dupename in self.dupes:
                game.getWorld().deleteItemsWithName(dupename)

        else:
            game.getWorld().deleteItemsWithName(self.name)


        '''
        if (self.dupes != []):
            for i in self.dupes:
                for j in game.world.rooms:
                    for k in range(len(j.items)):
                        if (j.items[k].name == i):
                            j.items.pop(k)'''

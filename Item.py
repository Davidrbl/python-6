class Item:
    def __init__(self, _name, dupes):
        self.name = _name
        self.dupes = dupes

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

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

class Item:
    def __init__(self, _name, dupes=[]):
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

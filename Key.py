from Item import Item

class Key(Item):
    def __init__(self, _name, _place, _room1, _room2, _dupes):
        super().__init__(_name, _place, _dupes)
        self.room1 = _room1
        self.room2 = _room2

    def onPickup(self, game):
        Item.onPickup(self, game)
        game.world.addExitsTo(self.room1, self.room2)

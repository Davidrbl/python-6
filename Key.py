from Item import Item

class Key(Item):
    def __init__(self, _name, _room1, _room2, _dupes):
        super().__init__(_name, _dupes)
        self.room1 = _room1
        self.room2 = _room2

    def onPickup(self, game):
        Item.onPickup(self, game)
        for i in self.room1:
            for j in self.room2:
                game.world.rooms[i].add_exit(game.world.rooms[j])
                game.world.rooms[j].add_exit(game.world.rooms[i])

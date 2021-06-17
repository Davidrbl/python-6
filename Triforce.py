from Item import Item

class Triforce(Item):
    def __init__(self, _name):
        super().__init__(_name, [])

    def onPickup(self, game):
        Item.onPickup(self,game)
        game.printHeader()
        game.printRegel("You picked up the " + self.name + "!")
        game.printFooter()
        triforceCounter = 0
        for i in game.getPlayer().getInventory():
            if type(i) == Triforce:
                triforceCounter += 1

        if (triforceCounter >= game.getTriforcecount()):
            game.notDone = False

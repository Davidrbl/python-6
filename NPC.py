from Item import Item

class NPC(Item):
    def __init__(self, _name, _dialogue, _gift=None):
        words = _dialogue.split()
        doneDialogue = []
        currentLine = ''
        i = 0
        while i < len(words):
            if len(currentLine) + len(words[i]) > 70 - 5:
                doneDialogue.append(currentLine)
                currentLine = ''
            else:
                currentLine += words[i] + ' '
                i += 1

        doneDialogue.append(currentLine)

        self.name = _name
        self.dialogue = doneDialogue
        self.gift = _gift
        self.talkedto = False


    def onTalk(self, game):
        game.printHeader()
        game.printRegel(self.name + " zegt:")
        for i in self.dialogue:
            game.printRegel(i)
        game.printFooter()

        if self.gift != None and not self.talkedto:
            self.gift.onPickup(game)
            self.talkedto = True

            game.player.inventory.append(self.gift)
            game.printHeader()
            game.printRegel(self.name + " gifted you " + self.gift.name)
            game.printFooter()

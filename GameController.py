from World import World
from Player import Player
import os

class GameController:
    def play_game(self):
        #hier input n shit doen
        while self.notDone:
            cr=self.player.get_current_room()

            cr.describe(self)

            inputs = input("Wat wil je doen?").split(" ", 1)
            self.clear()

            try:
                if (len(inputs)>3):
                    self.printHeader()
                    self.printRegel("Fout bij length check")
                    self.printFooter()
                    raise Exception
                elif (inputs[0] == self.comms[0]): #PICKUP
                    self.printHeader()
                    self.printRegel("picking up :" + inputs[1])
                    self.printFooter()
                    self.player.pick_up(inputs[1], cr, self)
                elif (inputs[0] == self.comms[1]): #GOTO
                    self.player.goto_room(inputs[1])
                elif (inputs[0] == self.comms[2]): #INVENTORY
                    self.printHeader()
                    self.printRegel(self.show_list(self.player.inventory, "Items"))
                    self.printFooter()
                elif (inputs[0] == self.comms[3]): #TALKTO
                    self.player.talkTo(inputs[1], self)
                elif (inputs[0] == self.comms[4]): #HELP
                    self.printHeader()
                    for i in range(len(self.comms)):
                        self.printRegel(self.comms[i] + " : " + self.commdesc[i])
                    self.printFooter()
                else:
                    raise Exception
            except Exception as error:
                self.printHeader()
                self.printRegel("ERROR: probeer het nog een keer.")
                #self.printRegel(error)
                self.printFooter()
        else:
            #PLAYER WON
            self.printHeader()
            self.printRegel("YOU WON!!!")
            self.printRegel("Jij, " + self.player.getName() + ", hebt de drie delen van de triforce gepakt!")
            self.printRegel("")
            self.printRegel("GOED GEDAAN!!")
            self.printFooter()


    def show_list(self, list, showing):
        inventstring = showing+': '
        for i in list:
            inventstring += i.name + ', '

        return inventstring[:len(inventstring) - 2]


    def printRegel(self, regel):
        print(("| {:" + str(self.schermbreedte - 4) + "} |").format(regel))

    def printHeader(self):
        print("_"*self.schermbreedte)
        print("| " + " "*int(self.schermbreedte - 4) + " |")

    def printFooter(self):
        print("| " + " "*int(self.schermbreedte - 4) + " |")
        print("|_" + "_"* int(self.schermbreedte - 4) + "_|")

    def clear(self):
        os.system('cls')

    def getWorld(self):
        return self.world

    def getPlayer(self):
        return self.player

    def getTriforcecount(self):
        return self.triforcecount

    def readWorldfromXML(self):
        self.printHeader()
        self.printRegel('Which file would you like to read from?')
        self.printFooter()
        filename = input()
        with open('maps/' + filename + '.xml', 'r') as file:
            text = file.read()
            lines = text.split("\n")
            numlines = len(lines)

            roombeginindexes = []
            roomendindexes = []
            #lines = file.readlines()

            try:
                '''
                roomcount = 0
                for lineIndex in range(numlines):
                    if "<Room>" in lines[lineIndex]:
                        roomcount += 1
                        roombeginindexes.append(lineIndex)

                for lineIndex in range(numlines):
                    if "</Room>" in lines[lineIndex]:
                        roomcount += 1
                        roomendindexes.append(lineIndex)

                for i in range(len(roombeginindexes)):
                    self.readRoomFromLines(lines, roombeginindexes[i], roomendindexes[i])

                print(roomcount)
                print(lines)
                input()
                '''
                roomcount = 0

                beginindex = 0
                roombeginindexes = []
                while(beginindex is not 0):
                    beginindex = text.find("<Room>", beginindex)
                    print("peepee"+str(beginindex))
                    roombeginindexes.append(beginindex)
                    beginindex += 1


                roombeginindexes.pop(len(roombeginindexes)-1)

                print(roombeginindexes)

                print("i am donzo")


            except Exception as err:
                print("you sussy baka, that's not a valid file!!!!")
                print(err)
                input()

            file.close()

    def readRoomFromLines(self, lines,beginindex, endindex):
        roomname = ''
        roomitems = []
        roompeople = []
        roomexits = []

        '''
        for lineIndex in range(beginindex, endindex+1):
            if lines[lineIndex] == '<Name>' and lines[lineIndex+2] == '</Name>':
                roomname = lines[lineindex+1]
            if lines[lineIndex] == '<Exits>' and lines[lineIndex+2] == '</Exits>':
                #roomexits.append(lines[])
                pass
            print(lines[lineIndex])
        '''

    def __init__(self):
        self.schermbreedte = 70
        self.clear()
        self.readWorldfromXML()
        self.clear()
        self.notDone = True

        self.comms = ["pickup",
                      "goto",
                      "inventory",
                      "talkto",
                      "help"]
        self.commdesc = ["Use to pick up item in current room",
                         "Use to go through an exit",
                         "Use to see your inventory",
                         "Ues to talk to people in the current room",
                         "Use to see all commands"]

        self.triforcecount = 3

        self.printHeader()
        self.printRegel("What is your name?")
        self.printFooter()
        playerName = input()
        self.clear()


        self.world = World()
        self.world.create_world()

        self.player = Player(playerName)
        self.player.set_current_room(self.world.first_room())

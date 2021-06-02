from GameController import GameController

#Cave           to: [River, Town]                       index=0
#River          to: [Cave, Forest, Wizard's Lab]        index=1
#Town           to: [Cave, Mountains, Wizard's Lab]     index=2
#Forest         to: [River, Castle, Wizard's Lab]       index=3
#Mountains      to: [Town, Castle, Wizard's Lab]        index=4
#Castle         to: [Forest, Mountains]                 index=5
#Wizard's Lab   to: [River, Town, Forest, Mountains]    index=6

game = GameController()
game.play_game()

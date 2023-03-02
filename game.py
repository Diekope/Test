from player import Player
from helpers import clear
import random

class Game:
    def __init__(self, player1: Player, player2: Player, player3: Player, player4: Player):
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.previous_card = None

    #Jeu
    def play(self):

        while not self.check_winning():
            print("Joueur 1, choisissez une carte. ")
            self.player1.print_cards()
            self.previous_card = self.player1.prompt_card(self.previous_card)

            clear()
            print("Joueur 2, choisissez une carte. ")
            self.player2.print_cards()
            self.previous_card = self.player2.prompt_card(self.previous_card)

            clear()
            print("Joueur 3, choisissez une carte. ")
            self.player3.print_cards()
            self.previous_card = self.player3.prompt_card(self.previous_card)

            clear()
            print("Joueur 4, choisissez une carte. ")
            self.player4.print_cards()
            self.previous_card = self.player4.prompt_card(self.previous_card)

    #Affiche le gagnant
    def check_winning(self):
        if len(self.player1.cards) == 0:
            print("Joueur 1 à gagné !")
            return True
        elif len(self.player2.cards) == 0:
            print("Joueur 2 à gagné !")
            return True
        elif len(self.player3.cards) == 0:
            print("Joueur 3 à gagné !")
            return True
        elif len(self.player4.cards) == 0:
            print("Joueur 4 à gagné !")
            return True
        else:
            return False
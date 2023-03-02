from termcolor import colored
from helpers import creat_all_cards
import random

#Création du joueur
class Player:
    #Initialisation
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.deck = create_all_cards()

    #Affichage smooth des cartes
    def print_cards(self):
        for card in self.cards:
            print(colored(card.get_card_text(), card.color))

    #Demande la carte au joueur
    def prompt_card(self, previous_card):
        if previous_card != None:
            print("La carte précédente est : " + colored(previous_card.get_card_text(), previous_card.color))
        card = input("Entrez la carte que vous voulez jouer : (format: numéro/nom - color). Si il n'y a pas de bonnes cartes, veuillez piocher en écrivant 'draw' :")
        while not self.check_card_valid(card, previous_card):
            print("Carte non trouvée ou invalide !")
            card = input("Entrez la carte que vous voulez jouer : (format: numéro/nom - color). Si il n'y a pas de bonnes cartes, veuillez piocher :")
        return self.remove_card(card)

    #Vérifie que la carte existe et peut être jouée
    def check_card_valid(self, card: str, previous_card):
        for c in self.cards:
            if previous_card != None:
                if str(c) == card and (previous_card.color == c.color or previous_card.number == c.number):
                    return True
            else:
                if str(c) == card:
                    return True
        return False

    #On supprime une carte
    def remove_card(self, card: str):
        for c in self.cards:
            if str(c) == card:
                self.cards.remove(c)
                return c

    #Pioche
    def draw_card(self, card):
        self.deck[random.randint(0, len(self.deck)-1)]        
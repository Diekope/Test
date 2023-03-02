from cards import Card
from subprocess import call
import os

#Création des cartes
def create_all_cards():
    deck = []
    for color in ["red","green","blue","yellow"]:
        for number in range (1,10):
            deck.append(Card(color,number, None))
#           for special_ability in ["skip","reverse","block","swap_simple","+2","+4","+6"]:
#               deck.append(Card(color, special_ability = special_ability))
                
#   deck.append(Card(special_ability="+10"))
#   deck.append(Card(special_ability="+10"))
#   deck.append(Card(special_ability="joker"))
#   deck.append(Card(special_ability="+joker"))
#   deck.append(Card(special_ability="swap_general"))
#   deck.append(Card(special_ability="swap_general"))

    print(len(deck))
    return deck

#Efface les cartes
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
class Card:
    #Création des cartes
    def __init__(self,color="white",number=0,special_ability=None):
        self.color = color
        self.number = number
        self.special_ability = special_ability

    #Affichage des cartes
    def __str__(self):
        return f"{self.get_card_text()} - {self.color}"

    def __repr__(self):
        return f"{self.get_card_text()} - {self.color}"

    def get_card_text(self):
        if self.number == 0:
            return self.special_ability
        else:
            return self.number

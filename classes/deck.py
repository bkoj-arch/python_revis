from classes.carte import *
import random


class Deck():
    def __init__(self):
        self.cartes=[]
        for col in Carte.couleurs:
            for val in range(1,14):
                self.cartes.append(Carte(val,col))
    
    def display_deck(self):
        for c in self.cartes:
           c.show_card()
        
        print("nb cartes: ", len(self.cartes))

    def drop_card(self):   
        return self.cartes.pop(random.randrange(len(self.cartes)))

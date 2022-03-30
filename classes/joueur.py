from classes.carte import *

class Joueur():
    def __init__(self,name):
        self.name=name
        self.main=[]
        self.points=0
        self.active_card=None

    def add_carte(self,cart):
        self.main.append(cart)

    def show_hand(self):
        print(self.name)

        i=1
        for c in self.main:
            symb=c.valeur
            if symb>10:
                symb=Carte.tetes[str(symb)]

            print(i," -- ",symb, "    ",c.couleur )
            i+=1

    def drop_card(self,ind):
        return self.main.pop(ind-1)

    def add_active_card(self,cart):
        self.active_card=cart
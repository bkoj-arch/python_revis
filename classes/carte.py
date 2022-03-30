class Carte():


    tetes={
        "11":"V",
        "12":"D",
        "13":"R"
    }

    # valeurs possible as -> roi
    min_val=1
    max_val=13

    #couleurs possible
    couleurs=["trefle","coeur","carreau","pique"]

    def __init__(self,val,coul):

        if val>=Carte.min_val and val<=Carte.max_val:
            self.valeur=val
        self.couleur=coul
    
    def show_card(self):
        symb=self.valeur
        if symb>10:
            symb=Carte.tetes[str(symb)]

        print(symb,"   ",self.couleur)
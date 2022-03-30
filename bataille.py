from classes.carte import *
from classes.deck import *
from classes.joueur import *


deck1=Deck()
deck1.display_deck()



j1=Joueur("Dorian")
j2=Joueur("Flavie")

players=[j1,j2]

for i in range(10):
    j1.add_carte(deck1.drop_card())
    j2.add_carte(deck1.drop_card())


while len(deck1.cartes)>0:

    for j in players:
        print("######################")
        print("######################")
        print()
        print("Vous avez",j.points, "points")
        j.show_hand()
        choix=input("Quelle carte voulez vous poser?: ")
        j.add_active_card(j.drop_card(int(choix)))
        print("Vous posez la carte: ",j.active_card.valeur,j.active_card.couleur)

        
    print("")
    print("######################")
    print()
    print("Il y a sur la table:")


    for j in players:
        print( j.active_card.valeur,j.active_card.couleur )

    print("")
    print("######################")
    print()
   
    if players[0].active_card.valeur<players[1].active_card.valeur:
        print(players[1].name, " Gagne la manche")
        players[1].points+=1

    elif players[0].active_card.valeur>players[1].active_card.valeur:
        print(players[0].name, " Gagne la manche")
        players[0].points+=1
    else:
        print("Egalité")

    
    for j in players:
        j.add_carte(deck1.drop_card())



if j1.points>j2.points:
    print("Bravo",j1.name)
elif j1.points<j2.points:
    print("Bravo",j2.name)
else:
    print("vous avez tous les deux bien joué")
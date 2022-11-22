import random

#Ici je debute le loop et je
running = True
niveau_vie = 20
victoires = 0
defaites = 00
while running:

    niveau_adversaire = random.randint(0,5)

    print("Vous tombez face à face avec un adversaire de difficulté :", niveau_adversaire)
    choix = int(input(
        "Que voulez-vous faire ? 1- Combattre cet adversaire, 2- Contourner cet adversaire et aller ouvrir une autre porte, 3- Afficher les règles du jeu, 4- Quitter la partie"))


    if choix == 2:
        niveau_vie -= 1
        print("vous avez", niveau_vie, "vies")
        niveau_adversaire = random.randint(0,5)

    if choix == 1:
        Attaque_joueur = random.randint(1,6)
        print("vous avez une force de", Attaque_joueur)
        if niveau_adversaire >= Attaque_joueur:
            niveau_vie -= niveau_adversaire
            print("vous avez",niveau_vie,"vies")

        elif niveau_adversaire <= Attaque_joueur:
            niveau_vie += niveau_adversaire
            victoires += 1
            print("vous avez", victoires,"victoires")
            print("vous avez", niveau_vie, "vies")

    if choix == 3:
        print( "Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.La partie se termine lorsque les points de vie de l’usager tombent sous 0.L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
        print("Vous tombez face à face avec un adversaire de difficulté :", niveau_adversaire)
        choix = int(input("Que voulez-vous faire ? 1- Combattre cet adversaire, 2- Contourner cet adversaire et aller ouvrir une autre porte, 3- Afficher les règles du jeu, 4- Quitter la partie"))




    if choix == 4:
        print("Merci et au revoir...")
        running =False

if niveau_vie <= 0:
    running =False
    print("vous etes mort")

import random





    

if choix == 3:
    print("les regles sont simples, tu te promene dans un dongeon, et tu combat des monstre. leur force est determiner par un nombre aleatoire entre 1 et 5, et tu devrai rouler un de pour le combattre")
    choix = input("Que voulez-vous faire ? n1- Combattre cet adversaire, 2- Contourner cet adversaire et aller ouvrir une autre porte, 3- Afficher les règles du jeu, 4- Quitter la partie")

running = True


while running:
    
    victoires = 0
    niveau_vie = 20
    niveau_adversaire = random.randint(0.5)

    print("Vous tombez face à face avec un adversaire de difficulté :", niveau_vie_adversaire)
    choix = int(input(
        "Que voulez-vous faire ? 1- Combattre cet adversaire, 2- Contourner cet adversaire et aller ouvrir une autre porte, 3- Afficher les règles du jeu, 4- Quitter la partie"))

    if choix == 2:
        niveau_vie -= 1
        niveau_adversaire = random.randint(0.5)

    if choix == 1:
        Attaque_joueur = random.randint(0.6)
        if force_adversaire >= Attaque_joueur:
            niveau_vie -= force_adversaire
            print(niveau_vie)

        elif force_adversaire <= Attaque_joueur:
            niveau_vie += force_adversaire

            if choix == 3:
                print(
                    "les regles sont simples, tu te promene dans un dongeon, et tu combat des monstre. leur force est determiner par un nombre aleatoire entre 1 et 5, et tu devrai rouler un de pour le combattre")
                choix = input(
                    "Que voulez-vous faire ? n1- Combattre cet adversaire, 2- Contourner cet adversaire et aller ouvrir une autre porte, 3- Afficher les règles du jeu, 4- Quitter la partie")

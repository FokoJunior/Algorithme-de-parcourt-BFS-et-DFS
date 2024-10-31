def dfs_iteratif(matrice_adj, sommet_depart, marques_globales):
    """
    Fonction récursive pour effectuer le parcours en profondeur (DFS) sur un graphe.
    - matrice_adj : matrice d'adjacence représentant le graphe
    - sommet_DEPART : sommet actuel pour le parcours
    - marques_globales : liste des sommets déjà marqués
    """
    """Effectue une recherche en profondeur itérative en respectant les noms et la structure de l'algorithme spécifié."""
    nombre_sommets = len(matrice_adj)
    pile = []
    chemin = [None] * nombre_sommets
    predecesseur = [None] * nombre_sommets
    etape = 0
    S0 = sommet_depart - 1

    # Initialisation
    pile.append(S0)
    marques_globales[S0] = 1
    chemin[S0] = etape

    while pile:
        etape += 1
        S0 = pile[-1]  # Sommet en haut de la pile
        successeur_trouve = False

        # Parcours des successeurs de S0
        for Sj in range(nombre_sommets):
            if matrice_adj[S0][Sj] == 1 and marques_globales[Sj] == 0:
                pile.append(Sj)
                marques_globales[Sj] = 1
                predecesseur[Sj] = S0
                chemin[Sj] = etape
                successeur_trouve = True
                break

        if not successeur_trouve:
            pile.pop()  # Dépiler si tous les successeurs sont déjà marqués
            marques_globales[S0] = 2  # Marquer le sommet comme terminé

    return chemin, predecesseur

def main():
    # Saisie du nombre de sommets et de la matrice d'adjacence
    n = int(input("Entrez le nombre de sommets: "))
    print("\nEntrez la matrice d'adjacence (0 pour non connecté, 1 pour connecté):")
    matrice_adj = [list(map(int, input(f"Ligne {i + 1}: ").strip().split())) for i in range(n)]

    # Initialisation des marques globales pour éviter le double marquage
    marques_globales = [0] * n

    while True:
        sommet_depart = int(input("\nEntrez le sommet de départ (1 à {}), ou -1 pour terminer: ".format(n)))
        if sommet_depart == -1:
            break
        if 1 <= sommet_depart <= n:
            if marques_globales[sommet_depart - 1] == 1:
                print(f"\nSommet {sommet_depart} déjà marqué dans un parcours précédent.")
                continue
            chemin, predecesseur = dfs_iteratif(matrice_adj, sommet_depart, marques_globales)
            print(f"\n\nRésultats pour DFS({sommet_depart}):")
            for i in range(n):
                if chemin[i] is not None:
                    print(f"Sommet: {i + 1}, Étape: {chemin[i]}, Prédécesseur: {predecesseur[i] + 1 if predecesseur[i] is not None else 'None'}")
        else:
            print("Sommet invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

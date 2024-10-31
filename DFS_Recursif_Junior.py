def dfs_recursif(matrice_adj, sommet, marques, composante):
    """
    Fonction récursive pour effectuer le parcours en profondeur (DFS) sur un graphe.
    - matrice_adj : matrice d'adjacence représentant le graphe
    - sommet : sommet actuel pour le parcours
    - marques : liste des sommets déjà marqués
    - composante : liste pour stocker les sommets visités dans cette composante
    """
    marques[sommet] = True
    composante.append(sommet + 1)  # Ajouter le sommet à la composante

    for successeur in range(len(matrice_adj[sommet])):
        if matrice_adj[sommet][successeur] == 1 and not marques[successeur]:
            dfs_recursif(matrice_adj, successeur, marques, composante)

    return composante

def main():
    # Saisie du nombre de sommets et de la matrice d'adjacence
    nombre_sommets = int(input("Entrez le nombre de sommets : "))
    print("\nEntrez la matrice d'adjacence (0 pour non connecté, 1 pour connecté) :")
    matrice_adj = [list(map(int, input(f"Ligne {i + 1} : ").split())) for i in range(nombre_sommets)]

    # Initialiser le tableau de marquage
    marques = [False] * nombre_sommets

    while True:
        # Demander le sommet de départ ou "terminer" pour arrêter
        entree = input("\nEntrez le sommet de départ (ou tapez 'terminer' pour finir) : ")
        if entree.lower() == "terminer":
            break
        
        sommet_depart = int(entree) - 1
        if 0 <= sommet_depart < nombre_sommets and not marques[sommet_depart]:
            composante = dfs_recursif(matrice_adj, sommet_depart, marques, [])
            print(f"Composante marquée à partir du sommet {sommet_depart + 1} : {composante}")
        elif 0 <= sommet_depart < nombre_sommets:
            print(f"Le sommet {sommet_depart + 1} est déjà marqué.")
        else:
            print("Sommet de départ invalide.")

if __name__ == "__main__":
    main()

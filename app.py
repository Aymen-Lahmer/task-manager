
taches = []

def ajouter_tache():
    tache = input("Entrez une tâche : ")
    taches.append(tache)
    print("Tâche ajoutée avec succès !")

ajouter_tache()

print("Liste des tâches :", taches)

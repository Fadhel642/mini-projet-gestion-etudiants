# script principal
# Ajouter un étudiant
def ajouter_etudiant(etudiants, id_, nom, prenom, notes):
    if id_ in etudiants:
        print("❌ ID déjà utilisé")
        return
    etudiants[id_] = {
        "id": id_,
        "nom": nom,
        "prenom": prenom,
        "notes": notes
    }
    print("✅ Étudiant ajouté :", nom, prenom)

# Supprimer un étudiant
def supprimer_etudiant(etudiants, id_):
    if id_ in etudiants:
        etudiants.pop(id_)
        print(f"✅ Étudiant {id_} supprimé")
    else:
        print("❌ ID introuvable")

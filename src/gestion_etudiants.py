# script principal
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

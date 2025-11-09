# script principal

import json
MATIERES_DISPONIBLES = frozenset({"Math", "Python", "Physique", "Anglais"})


# Ajouter un étudiant
def ajouter_etudiant(etudiants, set_ids, id_, nom, prenom, notes):
    if id_ in set_ids:
        print("ID déjà utilisé")
        return
    
    # Vérification des matières
    for matiere, note in notes:
        if matiere not in MATIERES_DISPONIBLES:
            print(f"Matière '{matiere}' non autorisée. Matières valides: {MATIERES_DISPONIBLES}")
            return
   
    etudiants[id_] = {
        "id": id_,
        "nom": nom,
        "prenom": prenom,
        "notes": notes
    }
    set_ids.add(id_)
    print("Étudiant ajouté :", nom, prenom)

# Supprimer un étudiant
def supprimer_etudiant(etudiants, set_ids, id_):
    if id_ in etudiants:
        etudiants.pop(id_)
        set_ids.remove(id_)
        print(f"Étudiant {id_} supprimé")
    else:
        print("ID introuvable")

# Modifier les notes
def modifier_notes(etudiants, id_, matiere, nouvelle_note):
    if id_ not in etudiants:
        print("ID introuvable")
        return
    
    if matiere not in MATIERES_DISPONIBLES:
        print(f"Matière '{matiere}' non autorisée. Matières valides: {MATIERES_DISPONIBLES}")
        return
    
    notes = etudiants[id_]["notes"]
    
    # Chercher si la matière existe déjà
    for i, (m, n) in enumerate(notes):
        if m == matiere:
            notes[i] = (matiere, nouvelle_note)  # on met à jour
            print(f"Note mise à jour pour {matiere}: {nouvelle_note}")
            return
    



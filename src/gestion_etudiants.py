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

# Modifier les notes
def modifier_notes(etudiants, id_, matiere, nouvelle_note):
    if id_ not in etudiants:
        print("❌ ID introuvable")
        return
    
    notes = etudiants[id_]["notes"]
    
    # Chercher si la matière existe déjà
    for i, (m, n) in enumerate(notes):
        if m == matiere:
            notes[i] = (matiere, nouvelle_note)  # on met à jour
            print(f"✅ Note mise à jour pour {matiere}: {nouvelle_note}")
            return
    
    # Si on n'a pas trouvé, on ajoute une nouvelle matière
    notes.append((matiere, nouvelle_note))
    print(f"✅ Nouvelle matière ajoutée : {matiere} ({nouvelle_note})")


# Statistiques & Calculs
def moyenne_etudiant(etudiants, id_):
    if id_ not in etudiants:
        print("❌ ID introuvable")
        return None
    
    notes = etudiants[id_]["notes"]
    if not notes:  # si pas de notes
        print("⚠️ Pas de notes pour cet étudiant")
        return None
    
    total = sum(note for (_, note) in notes)
    moyenne = total / len(notes)
    return round(moyenne, 2)  # arrondi à 2 décimales

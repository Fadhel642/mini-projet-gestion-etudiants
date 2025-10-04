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

def moyennes_par_matiere(etudiants):
    if not etudiants:
        print("❌ Aucun étudiant dans la base")
        return {}

    # dictionnaire pour accumuler les totaux
    totaux = {}
    comptes = {}

    for e in etudiants.values():
        for matiere, note in e["notes"]:
            totaux[matiere] = totaux.get(matiere, 0) + note
            comptes[matiere] = comptes.get(matiere, 0) + 1

    # calcul des moyennes
    moyennes = {m: round(totaux[m] / comptes[m], 2) for m in totaux}
    return moyennes

def moyenne_promotion(etudiants):
    if not etudiants:
        print("❌ Aucun étudiant dans la base")
        return None

    moyennes = []
    for id_, e in etudiants.items():
        notes = e["notes"]
        if notes:  # éviter les étudiants sans notes
            total = sum(note for (_, note) in notes)
            moy = total / len(notes)
            moyennes.append(moy)

    if not moyennes:
        return None

    return round(sum(moyennes) / len(moyennes), 2)

def etudiants_moyenne_sup(etudiants, seuil=15):
    resultats = []
    for id_, e in etudiants.items():
        notes = e["notes"]
        if notes:
            total = sum(note for (_, note) in notes)
            moy = total / len(notes)
            if moy > seuil:
                resultats.append((id_, e["nom"], e["prenom"], round(moy, 2)))
    return resultats

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

def classement(etudiants):
    resultats = []
    for id_, e in etudiants.items():
        notes = e["notes"]
        if notes:
            total = sum(note for (_, note) in notes)
            moy = total / len(notes)
        else:
            moy = 0  # si pas de notes, moyenne = 0
        resultats.append((id_, e["nom"], e["prenom"], round(moy, 2)))
    
    # Tri par moyenne décroissante
    resultats.sort(key=lambda x: x[3], reverse=True)
    return resultats


# Rapport global & export (txt)

def generer_rapport(etudiants):
    rapport = {
        "total_etudiants": len(etudiants),
        "moyenne_promotion": moyenne_promotion(etudiants),
        "moyennes_par_matiere": moyennes_par_matiere(etudiants),
        "classement": classement(etudiants),
        "etudiants_sup_15": etudiants_moyenne_sup(etudiants, 15)
    }
    return rapport

def exporter_rapport(rapport, chemin="rapport_promotion.txt"):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("=== Rapport global ===\n")
        f.write(f"Nombre total d'étudiants : {rapport['total_etudiants']}\n")
        f.write(f"Moyenne générale de la promotion : {rapport['moyenne_promotion']}\n\n")

        f.write("-- Moyennes par matière --\n")
        for m, v in rapport["moyennes_par_matiere"].items():
            f.write(f"{m} : {v}\n")
        f.write("\n")

        f.write("-- Classement des étudiants --\n")
        for rang, (id_, nom, prenom, moy) in enumerate(rapport["classement"], start=1):
            f.write(f"{rang}. [{id_}] {nom} {prenom} - {moy}\n")
        f.write("\n")

        f.write("-- Étudiants avec moyenne > 15 --\n")
        for id_, nom, prenom, moy in rapport["etudiants_sup_15"]:
            f.write(f"[{id_}] {nom} {prenom} - {moy}\n")
    print(f"✅ Rapport exporté dans {chemin}")

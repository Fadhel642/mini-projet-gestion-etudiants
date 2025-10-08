# script principal

import json
MATIERES_DISPONIBLES = frozenset({"Math", "Python", "Physique", "Anglais"})


# Ajouter un étudiant
def ajouter_etudiant(etudiants, set_ids, id_, nom, prenom, notes):
    if id_ in set_ids:
        print("❌ ID déjà utilisé")
        return
    
    # Vérification des matières
    for matiere, note in notes:
        if matiere not in MATIERES_DISPONIBLES:
            print(f"❌ Matière '{matiere}' non autorisée. Matières valides: {MATIERES_DISPONIBLES}")
            return
   
    etudiants[id_] = {
        "id": id_,
        "nom": nom,
        "prenom": prenom,
        "notes": notes
    }
    set_ids.add(id_)
    print("✅ Étudiant ajouté :", nom, prenom)

# Supprimer un étudiant
def supprimer_etudiant(etudiants, set_ids, id_):
    if id_ in etudiants:
        etudiants.pop(id_)
        set_ids.remove(id_)
        print(f"✅ Étudiant {id_} supprimé")
    else:
        print("❌ ID introuvable")

# Modifier les notes
def modifier_notes(etudiants, id_, matiere, nouvelle_note):
    if id_ not in etudiants:
        print("❌ ID introuvable")
        return
    
    if matiere not in MATIERES_DISPONIBLES:
        print(f"❌ Matière '{matiere}' non autorisée. Matières valides: {MATIERES_DISPONIBLES}")
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
    total = len(etudiants)
    if total == 0:
        return {}
    
    # Moyennes par étudiant
    moyennes = []
    for e in etudiants.values():
        notes = e["notes"]
        if notes:
            moy = sum(note for _, note in notes) / len(notes)
        else:
            moy = 0
        moyennes.append((e["id"], e["nom"], e["prenom"], round(moy, 2)))
    
    # Classement
    classement = sorted(moyennes, key=lambda x: x[3], reverse=True)

    # Moyenne générale promo
    moyenne_promo = round(sum(m[3] for m in classement) / total, 2)

    rapport = {
        "total_etudiants": total,
        "moyenne_promotion": moyenne_promo,
        "classement": classement
    }
    return rapport

def exporter_rapport(rapport, chemin="rapport_promotion.txt"):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write("=== Rapport global ===\n")
        f.write(f"Nombre total d'étudiants : {rapport['total_etudiants']}\n")
        f.write(f"Moyenne générale de la promotion : {rapport['moyenne_promotion']}\n\n")

        f.write("-- Classement --\n")
        for rang, (id_, nom, prenom, moy) in enumerate(rapport["classement"], start=1):
            f.write(f"{rang}. [{id_}] {nom} {prenom} - {moy}\n")

        f.write("\n-- JSON-like --\n")
        f.write(json.dumps(rapport, indent=2, ensure_ascii=False))

    print(f"✅ Rapport exporté dans {chemin}")

def recherche_avancee(etudiants, nom_contient=None, matiere=None, note_min=None):
    resultats = []

    for e in etudiants.values():
        # Filtrage nom/prénom
        if nom_contient:
            if nom_contient.lower() not in (e["nom"] + " " + e["prenom"]).lower():
                continue

        # Moyenne générale
        notes = e["notes"]
        moy = sum(note for _, note in notes) / len(notes) if notes else None

        # Filtrage matière + note minimale
        if matiere:
            note_matiere = None
            for m, n in notes:
                if m == matiere:
                    note_matiere = n
                    break
            if note_matiere is None or (note_min is not None and note_matiere < note_min):
                continue
        else:
            if note_min is not None and (moy is None or moy < note_min):
                continue

        resultats.append({
            "id": e["id"],
            "nom": e["nom"],
            "prenom": e["prenom"],
            "moyenne": round(moy, 2) if moy is not None else None
        })

    # Tri par moyenne décroissante
    resultats.sort(key=lambda r: (r["moyenne"] or -1), reverse=True)
    return resultats


def menu():
    print("\n=== Système de Gestion des Étudiants ===")
    print("1. Ajouter un étudiant")
    print("2. Modifier les notes d’un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Afficher la moyenne d’un étudiant")
    print("5. Afficher les moyennes par matière")
    print("6. Afficher la moyenne de la promotion")
    print("7. Afficher les étudiants avec moyenne > 15")
    print("8. Afficher le classement")
    print("9. Générer et exporter le rapport")
    print("10. Recherche avancée")

    print("0. Quitter")


def main():
    etudiants = {}
    set_ids = set()

    while True:
        menu()
        choix = input("Votre choix : ").strip()

        match choix:
            case "1":
                try:
                    id_ = int(input("ID : "))
                    nom = input("Nom : ")
                    prenom = input("Prénom : ")
                    notes_txt = input("Notes (ex: Math,16;Python,14) : ")
                    notes = []
                    if notes_txt:
                        for couple in notes_txt.split(";"):
                            mat, note = couple.split(",")
                            notes.append((mat.strip(), float(note)))
                    ajouter_etudiant(etudiants,set_ids, id_, nom, prenom, notes)
                except ValueError:
                    print("❌ Erreur : ID ou note invalide. Veuillez réessayer.")
            case "2":
                try:
                    id_ = int(input("ID : "))
                    matiere = input("Matière : ")
                    note = float(input("Nouvelle note : "))
                    modifier_notes(etudiants, id_, matiere, note)
                except ValueError:
                    print("❌ Erreur : ID ou note invalide.")

            case "3":
                try:
                    id_ = int(input("ID : "))
                    supprimer_etudiant(etudiants, set_ids, id_)
                except ValueError:
                    print("❌ Erreur : ID invalide.")

            case "4":
                try:
                    id_ = int(input("ID : "))
                    moy = moyenne_etudiant(etudiants, id_)
                    if moy is not None:
                        print("Moyenne :", moy)
                except ValueError:
                    print("❌ Erreur : ID invalide.")

            case "5":
                print(moyennes_par_matiere(etudiants))

            case "6":
                print("Moyenne promo :", moyenne_promotion(etudiants))

            case "7":
                sup = etudiants_moyenne_sup(etudiants, 15)
                if sup:
                    for i, (id_, nom, prenom, moy) in enumerate(sup, start=1):
                        print(f"{i}. [{id_}] {nom} {prenom} - {moy}")
                else:
                    print("❌ Aucun étudiant trouvé avec moyenne > 15")

            case "8":
                for rang, (id_, nom, prenom, moy) in enumerate(classement(etudiants), start=1):
                    print(f"{rang}. [{id_}] {nom} {prenom} - {moy}")

            case "9":
                rapport = generer_rapport(etudiants)
                if rapport:
                    print("📊 Rapport global :", json.dumps(rapport, indent=2, ensure_ascii=False))
                    exporter_rapport(rapport)
                else:
                    print("❌ Aucun étudiant dans la base.")

            case "10":
                nom_filtre = input("Nom/Prénom contient (laisser vide pour ignorer) : ").strip() or None
                matiere = input("Matière (laisser vide pour ignorer) : ").strip() or None
                note_txt = input("Note minimale (laisser vide pour ignorer) : ").strip()
                note_min = float(note_txt) if note_txt else None

                res = recherche_avancee(etudiants, nom_filtre, matiere, note_min)
                if res:
                    print("🔎 Résultats :")
                    for i, r in enumerate(res, start=1):
                        moy = r["moyenne"] if r["moyenne"] is not None else "(pas de notes)"
                        print(f"{i}. [{r['id']}] {r['nom']} {r['prenom']} - Moyenne : {moy}")
                else:
                    print("❌ Aucun étudiant trouvé.")

            case "0":
                print("👋 Au revoir !")
                break

            case _:
                print("❌ Choix invalide")

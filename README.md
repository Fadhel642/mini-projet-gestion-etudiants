# Mini-Projet : Système de Gestion d’Étudiants (Python)

Ce projet est un mini-système développé en **Python 3.10+** permettant de gérer une base d’étudiants, leurs notes et d’analyser leurs performances.  
Il répond à un cahier des charges scolaire en appliquant des concepts fondamentaux de la programmation structurée et de la gestion de données.

---

## Fonctionnalités principales

- Ajouter un étudiant (avec vérification d’un ID unique et validation des matières)
- Modifier les notes d’un étudiant (mise à jour ou ajout d’une nouvelle matière)
- Supprimer un étudiant
- Calculer les moyennes :
  - Moyenne individuelle
  - Moyenne par matière
  - Moyenne générale de la promotion
- Afficher les étudiants ayant une moyenne supérieure à 15
- Afficher le classement général des étudiants
- Générer un rapport global avec :
  - Nombre total d’étudiants
  - Moyenne générale de la promotion
  - Classement par ordre de mérite
- Export automatique du rapport dans un fichier texte (`rapport_promotion.txt`)
- Recherche avancée par nom, matière ou note minimale
- Export du rapport au format JSON-like

---

## Technologies et concepts utilisés

- **Langage :** Python 3.10+
- **Structures de données :**
  - `dict` pour représenter les étudiants
  - `list` et `tuple` pour les notes
  - `set` pour garantir l’unicité des identifiants
  - `frozenset` pour stocker les matières disponibles (immutables)
- **Logique et contrôle :**
  - `match-case` pour le menu interactif
  - `try/except` pour la gestion des erreurs
  - Compréhensions de liste pour les calculs de moyennes
  - `enumerate()` pour un affichage numéroté clair

---

## Installation

Cloner le projet :

```bash
git clone https://github.com/Fadhel642/mini-projet-gestion-etudiants.git
cd mini-projet-gestion-etudiants
```
---

## Exécution

```
python src/gestion_etudiants.py
```
---

## Exemple

Des exemples d’exécution se trouvent dans le dossier `examples/`.

---

## Licence
[MIT Licence](LICENSE)

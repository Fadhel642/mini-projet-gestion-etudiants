# Rapport – Structures de données & choix techniques

## Structures principales
- **Étudiant** : dictionnaire avec les clés `id`, `nom`, `prenom`, `notes`
- **Unicité ID** : set d’identifiants
- **Notes** : liste de tuples (matière, note)
- **Matières disponibles** : frozenset (bonus)

## Contrôles et bonnes pratiques
- `match-case` pour le menu
- `list comprehensions` pour les moyennes
- `enumerate()` pour l’affichage
- `try/except` pour gérer erreurs

## Justification
- `dict` flexible pour stocker infos d’un étudiant
- `set` rapide pour vérifier l’unicité
- `frozenset` pour des matières immuables
- Stockage en mémoire (pas de base de données, respect des consignes)

## Exemple d’utilisation
Voir `examples/session.log`.

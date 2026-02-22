# Module serveur

Petit module serveur Flask pour le projet de calculatrice.

### Raison d'être

Ce répertoire contient l'application backend qui reçoit les requêtes du front-end, évalue des expressions arithmétiques simples et renvoie la page HTML avec le résultat.

### Fichiers principaux
- `app.py` : point d'entrée Flask, gestion de la route `/` et fonction `calculate()`.
- `operators.py` : implémentation des opérations de base (`add`, `subtract`, `multiply`, `divide`).

### Dépendances et hypothèses
- Python et pip.
- Flask.
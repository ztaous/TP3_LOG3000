# Module style (CSS)

Ce répertoire contient les styles CSS utilisés par la page de la calculatrice.

### Raison d'être

Fournir la mise en forme et le rendu visuel de l'interface HTML (boutons, champ d'affichage, mise en page).

### Fichiers principaux
- `style.css` : feuilles de style principales appliquées à `index.html`.

### Dépendances et hypothèses
- Le fichier est chargé via Flask avec `url_for('static', filename='style.css')`. Il doit être dans le dossier `static`.

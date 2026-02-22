# Module front-end (HTML)

Ce dossier contient l'interface utilisateur HTML de la petite calculatrice.

### Raison d'être

Fournir la page `index.html` affichée à l'utilisateur, permettre la saisie d'expressions et l'envoi du formulaire vers le serveur pour évaluation.

### Fichiers principaux
- `index.html` : page unique qui contient la structure de la calculatrice, les boutons, et un petit script JavaScript pour gérer l'affichage.

### Dépendances et hypothèses
- Le fichier utilise des placeholders Jinja (`{{ result }}`) et `url_for('static', ...)`. Il doit donc être servi par Flask.
- Le formulaire soumet un champ nommé `display` au serveur.
# Number Cruncher

Une petite application web de calculatrice avec Python et Flask.

## But et portée du projet

**Number Cruncher** est une application web minimaliste permettant d'effectuer les quatre opérations mathématiques de base (addition, soustraction, multiplication et division).

## Installation
### Prérequis
- `Git` installé localement
- `Python` et `pip` installé
### Instructions

1. **Cloner le projet** localement via le terminal :
```
git clone https://github.com/ztaous/TP3_LOG3000.git
cd TP3_LOG3000
```

2. **Créer un environnement virtuel** :
```
python -m venv venv
```

3. **Activer l'environnement virtuel** :
   - **Sur Linux/macOS** :
     ```
     ./venv/bin/activate
     ```
   - **Sur Windows** :
     ```
     ./venv/Scripts/activate
     ```

4. **Installer les dépendances** :
```
pip install flask
```

5. **Lancer l'application** :
```
cd src
flask run
```

L'application sera accessible à l'adresse `http://localhost:5000` dans votre navigateur.

## Utilisation

### Fonctionnalités principales

1. **Saisir une expression** : Cliquez sur les boutons numériques et d'opérateurs pour former une expression (ex. `5 + 3`).
2. **Calculer** : Cliquez sur le bouton `=` pour soumettre l'expression au serveur.
3. **Afficher le résultat** : Le serveur calcule et renvoie le résultat qui s'affiche dans le champ.
4. **Effacer** : Cliquez sur `C` pour réinitialiser l'affichage.

## Tests

Une suite de tests sera ajoutée au repositoire pour valider les opérations mathématiques et la logique de parsing.

### Comment exécuter les tests (à venir)

```
cd server
python -m pytest
```

À ce stade, vous pouvez tester l'application manuellement en entrant diverses expressions dans l'interface.

## Flux de contribution

Nous utilisons un modèle standard de branches et pull requests pour contribuer au projet. Voici comment participer :

### Branches

- **`main`** : branche stable, code principal.
- **`feature/nom-de-la-fonctionnalité`** : pour les nouvelles fonctionnalités (ex. `feature/add-exponentiation`).
- **`bugfix/description-du-bug`** : pour les corrections de bugs (ex. `bugfix/wrong-multiplication-operator`).

### Gestion des issues

- **Créer une issue** pour signaler un bug ou proposer une nouvelle fonctionnalité.
- **Lier une PR à une issue** : utilisez les mots-clés `Fixes #<numéro>`, `Closes #<numéro>`, ou `Relates to #<numéro>` dans la description de la PR.
- Les issues fermées par une PR fusionnée seront marquées comme résolues.

## Crédits

**Ce projet est développé par l'équipe 28** dans le cadre du cours de génie logiciel.

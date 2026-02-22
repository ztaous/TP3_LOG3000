# Tests pour Number Cruncher

On teste la fonction `calculate` dans `app.py` et aussi toutes les opérations dans `operators.py`.

## Fichiers de test

### `test_operators.py`
Les tests pour les opérations mathématiques dans `operators.py`:
- **TestAdd**: Tests pour `add(a, b)`
- **TestSubtract**: Tests pour `subtract(a, b)`
- **TestMultiply**: Tests pour `multiply(a, b)`
- **TestDivide**: Tests pour `divide(a, b)`

### `test_app.py`
Les tests pour la fonction `calculate(expr: str)` dans `app.py`:
- **TestCalculateValidExpressions**: Teste les expressions valides
- **TestCalculateInvalidExpressions**: Teste les expressions mal formées
- **TestCalculateDivisionByZero**: Teste la division par zéro
- **TestCalculateEdgeCases**: Teste les cas limites

## Comment lancer les tests

1. Installer Pytest:
```bash
pip install pytest
```

2. Lancer tous les tests depuis le dossier `src`:
```bash
pytest tests/
```

3. Lancer un fichier de tests spécifique
```bash
pytest tests/test_operators.py
pytest tests/test_app.py
```

4. Lancer une classe de tests
```bash
pytest tests/test_operators.py::TestAdd
pytest tests/test_app.py::TestCalculateValidExpressions
```

5. Lancer un seul test:
```bash
pytest tests/test_operators.py::TestAdd::test_add_positive_numbers
pytest tests/test_app.py::TestCalculateValidExpressions::test_addition
```

6. Lancer les tests avec plus de détails
```bash
pytest tests/ -v
```
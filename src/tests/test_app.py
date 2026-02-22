"""
Tests unitaires pour la fonction calculate dans app.py.

Les tests couvrent:
- Les expressions valides avec tous les opérateurs (+, -, *, /)
- Les cas limites (zéro, nombres négatifs, décimaux)
- Les entrées invalides (expressions malformées, opérateurs multiples, opérandes manquants)
- La gestion des erreurs
"""

import pytest
from app import calculate


class TestCalculateExpressionsValides:
    """Tests pour la fonction calculate avec des expressions correctes."""
    
    def test_addition_nombres_positifs(self):
        """L'addition doit retourner la somme de deux nombres positifs."""
        assert calculate("3 + 4") == 7
        assert calculate("10 + 5") == 15
    
    def test_addition_nombres_negatifs(self):
        """L'addition doit fonctionner avec des nombres négatifs."""
        assert calculate("-10 + -5") == -15
        assert calculate("5 + -3") == 2
    
    def test_addition_decimaux(self):
        """L'addition doit fonctionner avec des nombres à virgule."""
        assert calculate("1.5 + 2.5") == 4.0
        ## Imprécision de la représentation 0.1 donne 0.30000000000000004, on utilise pytest.approx pour comparer à 0.3
        assert calculate("0.1 + 0.2") == pytest.approx(0.3)
    
    def test_soustraction_nombres_positifs(self):
        """La soustraction doit retourner a - b."""
        assert calculate("5 - 2") == 3
        assert calculate("10 - 3") == 7
    
    def test_soustraction_nombres_negatifs(self):
        """La soustraction doit fonctionner avec des nombres négatifs."""
        assert calculate("-5 - 3") == -8
        assert calculate("10 - -5") == 15
    
    def test_soustraction_decimaux(self):
        """La soustraction doit fonctionner avec des décimaux."""
        assert calculate("5.5 - 2.5") == 3.0
        assert calculate("1.0 - 0.1") == pytest.approx(0.9)
    
    def test_multiplication_nombres_positifs(self):
        """La multiplication doit retourner a * b."""
        assert calculate("2 * 3") == 6
        assert calculate("5 * 2") == 10
    
    def test_multiplication_nombres_negatifs(self):
        """La multiplication doit fonctionner avec des nombres négatifs."""
        assert calculate("-2 * 3") == -6
        assert calculate("-5 * -2") == 10
    
    def test_multiplication_decimaux(self):
        """La multiplication doit fonctionner avec des décimaux."""
        assert calculate("2.5 * 2") == 5.0
        assert calculate("1.5 * 2") == 3.0
    
    def test_division_nombres_entiers(self):
        """La division doit retourner a / b."""
        assert calculate("10 / 2") == 5.0
        assert calculate("7 / 2") == 3.5
        assert calculate("9 / 4") == 2.25
    
    def test_division_nombres_negatifs(self):
        """La division doit fonctionner avec des nombres négatifs."""
        assert calculate("10 / -2") == -5.0
        assert calculate("-10 / -2") == 5.0
    
    def test_division_decimaux(self):
        """La division doit fonctionner avec des décimaux."""
        assert calculate("7.5 / 2.5") == 3.0
        assert calculate("7.0 / 2.5") == 2.8
    
    def test_espace_dans_expression(self):
        """Les espaces dans l'expression ne doivent pas poser de problème."""
        assert calculate("  3   +   4  ") == 7
        assert calculate("3+ 4") == 7

class TestCalculateExpressionsInvalides:
    """Tests pour la fonction calculate avec des expressions invalides."""
    
    def test_expression_vide(self):
        """Une expression vide doit lever une ValueError."""
        with pytest.raises(ValueError, match="empty expression"):
            calculate("")
        
        with pytest.raises(ValueError, match="empty expression"):
            calculate(None)
    
    def test_type_invalide(self):
        """Un type non-string doit lever une ValueError."""
        with pytest.raises(ValueError, match="empty expression"):
            calculate(123)
        
        with pytest.raises(ValueError, match="empty expression"):
            calculate(12.5)
    
    def test_pas_operateur(self):
        """Une expression sans opérateur doit lever une ValueError."""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("3 4")
        
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("42")
    
    def test_plusieurs_operateurs(self):
        """Une expression avec plusieurs opérateurs doit lever une ValueError."""
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("3 + 4 - 2")
        
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("10 * 2 / 5")
        
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("1 + 2 + 3")
    
    def test_operateur_debut(self):
        """Un opérateur mal placé doit lever une ValueError."""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+ 5")
        
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("10-")
    
    def test_operandes_non_numeriques(self):
        """Les opérandes doivent être des nombres."""
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("abc + 5")
        
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("a + b")
    
    def test_caracteres_invalides(self):
        """Les caractères invalides doivent lever une ValueError."""
        with pytest.raises(ValueError):
            calculate("3 @ 5")
        
        with pytest.raises(ValueError):
            calculate("3 & 5")
    
    def test_operandes_manquants(self):
        """Une expression juste avec un opérateur est invalide."""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+")


class TestCalculateDivisionParZero:
    """Tests pour les cas de division par zéro."""
    
    def test_division_par_zero(self):
        """Une division par zéro doit lever une ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            calculate("10 / 0")
        
        with pytest.raises(ZeroDivisionError):
            calculate("5 / 0")
        
        with pytest.raises(ZeroDivisionError):
            calculate("0 / 0")


class TestCalculateCasLimites:
    """Tests pour les cas limites et conditions de bord."""
    
    def test_tres_grands_nombres(self):
        """Les très grands nombres doivent fonctionner."""
        assert calculate("1000000 + 2000000") == 3000000
    
    def test_tres_petits_nombres(self):
        """Les très petits nombres décimaux doivent fonctionner."""
        result = calculate("0.1 + 0.2")
        assert pytest.approx(result) == 0.3
    
    def test_operations_avec_zero(self):
        """Les opérations avec zéro doivent être correctes."""
        assert calculate("0 - 5") == -5
        assert calculate("5 - 0") == 5
        assert calculate("0 * 5") == 0
        assert calculate("0 / 5") == 0.0

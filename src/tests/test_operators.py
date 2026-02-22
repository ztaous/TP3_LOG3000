"""
Tests unitaires pour le module operators.py.

Les tests couvrent:
- Les opérations avec des nombres positifs et négatifs
- Les opérations avec des entiers et décimaux
- Les opérations avec zéro
"""

import pytest
from operators import add, subtract, multiply, divide


class TestAdd:
    """Tests pour la fonction add."""
    
    def test_add_nombres_positifs(self):
        """L'addition de deux nombres positifs doit retourner leur somme."""
        assert add(2, 3) == 5
        assert add(0.5, 0.5) == 1.0
    
    def test_add_nombres_negatifs(self):
        """L'addition doit fonctionner avec des nombres négatifs."""
        assert add(-2, -3) == -5
        assert add(-5, 5) == 0
        assert add(-10, 20) == 10
    
    def test_add_avec_zero(self):
        """L'addition avec zéro doit retourner l'autre nombre."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0
    
    def test_add_decimaux(self):
        """L'addition doit fonctionner avec des nombres à virgule."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)
        assert add(-1.5, 1.5) == 0.0

class TestSubtract:
    """Tests pour la fonction subtract."""
    
    def test_subtract_nombres_positifs(self):
        """La soustraction doit retourner a - b."""
        assert subtract(5, 2) == 3
        assert subtract(0.5, 0.5) == 0.0
    
    def test_subtract_nombres_negatifs(self):
        """La soustraction doit fonctionner avec des nombres négatifs."""
        assert subtract(-2, -3) == 1
        assert subtract(-5, 5) == -10
        assert subtract(-10, 20) == -30
    
    def test_subtract_avec_zero(self):
        """La soustraction avec zéro doit être correcte."""
        assert subtract(0, 5) == -5
        assert subtract(5, 0) == 5
        assert subtract(0, 0) == 0
    
    def test_subtract_decimaux(self):
        """La soustraction doit fonctionner avec des décimaux."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(1.0, 0.1) == pytest.approx(0.9)

class TestMultiply:
    """Tests pour la fonction multiply."""
    
    def test_multiply_nombres_positifs(self):
        """La multiplication doit retourner a * b."""
        assert multiply(2, 3) == 6
        assert multiply(5, 2) == 10
    
    def test_multiply_par_zero(self):
        """La multiplication par zéro doit retourner zéro."""
        assert multiply(0, 5) == 0
        assert multiply(5, 0) == 0
    
    def test_multiply_par_un(self):
        """La multiplication par 1 doit être l'identité."""
        assert multiply(1, 5) == 5
        assert multiply(5, 1) == 5
    
    def test_multiply_nombres_negatifs(self):
        """La multiplication doit fonctionner avec des nombres négatifs."""
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
        assert multiply(-5, -2) == 10
    
    def test_multiply_decimaux(self):
        """La multiplication doit fonctionner avec des décimaux."""
        assert multiply(2.5, 2) == 5.0
        assert multiply(1.5, 2) == 3.0

class TestDivide:
    """Tests pour la fonction divide."""
    
    def test_divide_nombres_entiers(self):
        """La division doit retourner a / b."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(0, 5) == 0.0
    
    def test_divide_avec_reste(self):
        """La division doit retourner le résultat exact."""
        assert divide(7, 2) == 3.5
        assert divide(9, 4) == 2.25
    
    def test_divide_par_un(self):
        """La division par 1 doit être l'identité."""
        assert divide(5, 1) == 5.0
        assert divide(100, 1) == 100.0
    
    def test_divide_petit_par_grand(self):
        """Diviser un petit nombre par un grand doit retourner une fraction."""
        assert divide(2, 10) == 0.2
        assert divide(3, 9) == pytest.approx(1/3)
    
    def test_divide_nombres_negatifs(self):
        """La division doit fonctionner avec des nombres négatifs."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0
    
    def test_divide_numerateur_zero(self):
        """Diviser zéro par quelque chose doit retourner zéro."""
        assert divide(0, 5) == 0.0
    
    def test_divide_par_zero(self):
        """Diviser par zéro doit lever une erreur."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
    
    def test_divide_decimaux(self):
        """La division doit fonctionner avec des décimaux."""
        assert divide(10.0, 2.0) == 5.0
        assert divide(7.5, 2.5) == 3.0
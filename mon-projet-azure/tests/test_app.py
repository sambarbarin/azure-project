import sys
import os

# Ajout du dossier src au path pour permettre l'import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import additionner, saluer

def test_additionner():
    assert additionner(2, 3) == 5
    assert additionner(-1, 1) == 0

def test_saluer():
    assert saluer("Alice") == "Bonjour, Alice !"
    assert saluer("") == "Bonjour, invité !"

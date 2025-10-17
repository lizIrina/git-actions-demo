import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import reverse_text

from app import reverse_text

def test_reverse_basic():
    assert reverse_text("hola") == "aloh"

def test_reverse_empty():
    assert reverse_text("") == ""

def test_reverse_palindrome():
    assert reverse_text("liz") == "liz"

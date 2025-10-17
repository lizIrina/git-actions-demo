from app import reverse_text


# --- Tests ---
def test_reverse_basic():
    assert reverse_text("hola") == "aloh"


def test_reverse_empty():
    assert reverse_text("") == ""


def test_reverse_palindrome():
    assert reverse_text("ana") == "ana"

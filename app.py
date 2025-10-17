def reverse_text(s: str) -> str:
    """Devuelve la cadena invertida."""
    return s[::-1]


if __name__ == "__main__":
    text = input("Escribe algo: ")
    print(reverse_text(text))

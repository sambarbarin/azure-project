def additionner(a: int, b: int) -> int:
    return a + b

def saluer(nom: str) -> str:
    if not nom:
        return "Bonjour, invité !"
    return f"Bonjour, {nom} !"

if __name__ == "__main__":
    print(saluer("Azure DevOps"))
    print(f"2 + 3 = {additionner(2, 3)}")

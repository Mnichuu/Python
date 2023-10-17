def licz_wyrazy(napis):
    wyrazy = napis.split()
    return len(wyrazy)


napis = ("""Przykładowy
wielowierszowy 
napis.""")

print(f"Liczba wyrazów w napisie: {licz_wyrazy(napis)}")

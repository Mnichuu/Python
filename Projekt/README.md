# [Projekt zaliczeniowy (SNAKE)](snake2.py)
Jako projekt zaliczeniowy wybrałem wcześniej napisaną grę snake z [09](../09)

Do projektu zdecydowałem się dodać:
1. Ekran z logiem gry oraz wyborem trudności rozgrywki.
2. Ekran startowy.
3. Możliwość pauzy oraz zakończenia gry w dowolnym momencie.
4. Wyświetlanie aktualnego wyniku w oknie gry.
5. Możliwość zapisania swojego wyniku do pliku płaskie.
6. Podgląd 5 najlepszych wyników zapisanych (scoreboard).

# W jaki sposób zagrać?
Po pobraniu całej zawartości proszę otworzyć w terminalu katalog główny (Projekt) i wywołać ```python snake2.py```:<br>

```console
~/Python-repo/Projekt> python snake2.py
```
# Ogólny zarys projektu snake2
### Plik [snake2.py](snake2.py) zawiera wszystkie funkcjonalności gry snake2 takie jak:
1. Główne okno gry
2. Rysowanie obiektów
3. Ekran wyboru poziomu trudności
4. Ekran  startowy
5. Ekran pauzy
6. Ekran końcowy z tabelą wyników

# Definiowanie zmiennych
```python
from _operator import itemgetter

import pygame
import sys
import random
from datetime import datetime

# Ustawienia gry
WIDTH, HEIGHT = 800, 600
FPS = 10
BLOCK_SIZE = 20
APPLE_DURATION = 100

# Predefiniowane poziomy trudności
EASY = {"FPS": 10, "APPLE_DURATION": 100}
MEDIUM = {"FPS": 15, "APPLE_DURATION": 80}
HARD = {"FPS": 20, "APPLE_DURATION": 60}

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRID_COLOR = (200, 200, 200)

# Kierunki
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
```

# Funkcje
```python
# Funkcja rysująca węża na ekranie, przechodzi przez cały segment węża i rysuje prostokąty
def draw_snake(snake):


# Funkcja rysująca jabłko na ekranie
def draw_apple(apple):
    pass


# Funkcja rysująca zatrute jabłko na ekranie
def draw_poison_apple(poison_apple):
    pass


# Funkcja przemieszczania węża po planszy
def move_snake(snake, direction, grow_tail=False):
    pass


# Losowe generowanie jabłka na ekranie z uwzględnieniem pozycji węża
def generate_apple(snake):
    pass


# Losowe generowanie jabłka na ekranie z uwzględnieniem pozycji węża
def generate_poison_apple(snake):
    pass


def start_screen():
    pass


# Funkcja odpowiedzialna z wyświetlanie tablicy wyników
def display_scoreboard():
    pass


# Funkcja odpowiedzialna za prowadzanie nicku + zapisywanie do pliku płaskiego
def save_score_with_nick(score):
    pass


# Funkcja zapisująca dane do pliku płaskiego
def save_score_with_nick_to_file(score, nick):
   pass


# Funkcja odpowiedzialna za wyświetlanie ilości punktów na koniec gry
def display_score(score):
    pass


# Funkcja wprowadzająca możliwość pauzowania gry
def pause_game(score):
   pass


# Wyświetlanie obecnego wyniku dynamicznie w oknie w trakcie gry
def display_current_score(score):
   pass


# Funkcja umożliwiająca wybór trudności gry
def select_difficulty():
    pass
```

# Główna pętla gry
Funkcja main() jest główną pętlą gry, która zarządza logiką rozgrywki, steruje interakcjami gracza, obsługuje zdarzenia oraz rysuje obiekty na ekranie.
Oprócz wywołań wyżej podanych funkcji główna pętla gry oczekuje na zdarzenia od gracza, aktualizuje kierunki ruchu, także sam ruch, węża zgodnie z wciskanymi klawiszami,
obsługuje kolizje z jabłkiem, zatrutym jabłkiem, węża z samym sobą i aktualizuje wynik, sprawdza periodyczne warunki brzegowe oraz umożliwa przenikanie węża przez ramkę gry.
```python
def main():
    pass

```



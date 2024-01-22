from _operator import itemgetter

import pygame
import sys
import random
from datetime import datetime

# Inicjalizacja Pygame
pygame.init()

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

# Inicjalizacja okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Inicjalizacja zegara
clock = pygame.time.Clock()


# Funkcja rysująca węża na ekranie, przechodzi przez cały segment węża i rysuje prostokąty
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))


# Funkcja rysująca jabłko na ekranie
def draw_apple(apple):
    pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], BLOCK_SIZE, BLOCK_SIZE))


# Funkcja rysująca zatrute jabłko na ekranie
def draw_poison_apple(poison_apple):
    pygame.draw.rect(screen, BLUE, pygame.Rect(poison_apple[0], poison_apple[1], BLOCK_SIZE, BLOCK_SIZE))


# Funkcja przemieszczania węża po planszy
def move_snake(snake, direction, grow_tail=False):
    new_head = (snake[0][0] + direction[0] * BLOCK_SIZE, snake[0][1] + direction[1] * BLOCK_SIZE)
    snake.insert(0, new_head)  # Dodanie nowej głowy na początek
    if not grow_tail:
        snake.pop()
    return True


# Losowe generowanie jabłka na ekranie z uwzględnieniem pozycji węża
def generate_apple(snake):
    while True:
        apple = (random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                 random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
        if apple not in snake:
            return apple


# Losowe generowanie jabłka na ekranie z uwzględnieniem pozycji węża
def generate_poison_apple(snake):
    while True:
        poison_apple = (random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
        if poison_apple not in snake:
            return poison_apple


def start_screen():
    font = pygame.font.Font(None, 36)  # Inicjalizacja czcionki
    text = font.render("Press any key to start", True, BLACK)  # Utworzenie tekstu
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Pozycja tekstu

    screen.fill(WHITE)  # Wypełnienie ekranu białym kolorem
    screen.blit(text, text_rect)  # Rysowanie tekstu na ekranie
    pygame.display.flip()  # Aktualizacja ekranu, aby pokazać wprowadzone zmiany

    # Oczekiwanie na naciśnięcie dowolnego klawisza
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                waiting_for_key = False


# Funkcja odpowiedzialna z wyświetlanie tablicy wyników
def display_scoreboard():
    scores = []

    try:
        with open("scores.txt", "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                name = parts[0]
                score = int(parts[1])
                date = parts[2]
                scores.append({"name": name, "score": score, "date": date})

        # Sortowanie wyników malejąco według wyników
        scores.sort(key=itemgetter("score"), reverse=True)

        font = pygame.font.Font(None, 36)
        text_y = 140

        # Wyświetlanie pięciu najlepszych wyników
        for i, entry in enumerate(scores[:5]):
            text = font.render(f"{i + 1}. {entry['name']}: {entry['score']}, Date: {entry['date']}", True, BLACK)
            screen.blit(text, (10, text_y))
            text_y += 40

        pygame.display.flip()

    except FileNotFoundError:
        print("Scores file not found.")


# Funkcja odpowiedzialna za prowadzanie nicku + zapisywanie do pliku płaskiego
def save_score_with_nick(score):
    # Inicjalizacja zmiennych
    font = pygame.font.Font(None, 36)
    end_text = font.render("Game over! Your score is: " + str(score), True, GREEN)
    text = font.render("Enter your nickname and press 'Enter' to save your score: ", True, GREEN)
    esc_text = font.render("Press 'Esc' to quit the game :) ", True, GREEN)
    screen.fill((128, 128, 128))
    screen.blit(end_text, (10, 10))
    screen.blit(text, (10, 50))

    pygame.display.flip()

    nick = ""
    saved = False
    while True:
        for event in pygame.event.get():
            display_scoreboard()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not saved:
                    if nick:
                        save_score_with_nick_to_file(score, nick)
                        screen.fill((128, 128, 128))
                        screen.blit(end_text, (10, 10))
                        screen.blit(esc_text, (10, 50))
                        saved = True
                elif event.key == pygame.K_BACKSPACE and not saved:
                    nick = nick[:-1]
                    screen.fill((128, 128, 128))
                    screen.blit(text, (10, 50))
                    screen.blit(end_text, (10, 10))
                elif event.key in range(pygame.K_a, pygame.K_z + 1) and not saved:
                    nick += event.unicode
                elif event.key in range(pygame.K_1, pygame.K_9 + 1) and not saved:
                    nick += event.unicode
                elif event.key == pygame.K_ESCAPE:
                    return

        nick_input_surface = font.render(nick, True, GREEN)
        screen.blit(nick_input_surface, (10, 90))
        pygame.display.flip()
        clock.tick(FPS)


# Funkcja zapisująca dane do pliku płaskiego
def save_score_with_nick_to_file(score, nick):
    with open("scores.txt", "a") as file:
        # czas
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write("{}, {}, {}\n".format(nick, score, timestamp))


# Funkcja odpowiedzialna za wyświetlanie ilości punktów na koniec gry
def display_score(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Score: {}".format(score), True, GREEN)
    screen.blit(text, (10, 10))


# Funkcja wprowadzająca możliwość pauzowania gry
def pause_game(score):
    # Inicjalizacja zmiennych
    font = pygame.font.Font(None, 36)
    text = font.render("Game paused. Press 'R' to resume or 'Q' to quit.", True, BLACK)

    # Tworzenie poweirzchni o rozmiarach całego okna
    background_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    background_surface.fill((128, 128, 128))  # Szary kolor tła
    background_surface.set_alpha(128)  # Przeźroczystość

    # Ustawienie prostokąta tekstu w środku ekranu
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    # Rysowanie tła i tekstu
    screen.blit(background_surface, (0, 0))  # Ustawienie tła na całe okno
    screen.blit(text, text_rect)

    # Odświeżenie ekranu
    pygame.display.flip()

    # Czekanie na odpowiedni przycisk
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score_with_nick(score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting_for_key = False
                elif event.key == pygame.K_q:
                    save_score_with_nick(score)
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)


# Wyświetlanie obecnego wyniku dynamicznie w oknie w trakcie gry
def display_current_score(score):
    # Inicjalizacja czcionki
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Current Score: {}".format(score), True, (0, 0, 0))

    # Tworzenie powierzchni dla tekstu z przeźroczystym szarym tłem
    background_surface = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
    background_surface.fill((128, 128, 128))  # Szary kolor tła
    background_surface.set_alpha(128)  # Przezroczystość

    # Rysowanie tła tekstu na ekranie
    screen.blit(background_surface, (WIDTH - 250, 10))
    screen.blit(text_surface, (WIDTH - 250, 10))


# Funkcja umożliwiająca wybór trudności gry
def select_difficulty():
    # Inicjalizacja czcionki i tekstu
    font = pygame.font.Font(None, 36)
    text = font.render("Select difficulty: E - Easy, M - Medium, H - Hard", True, GREEN)

    # Załadowanie logo gry
    snake_logo = pygame.image.load("SnakeLogo.png")

    # Pomniejszenie zdjęcia o połowę
    new_size = (snake_logo.get_width() // 2, snake_logo.get_height() // 2)
    snake_logo_resized = pygame.transform.scale(snake_logo, new_size)
    logo_rect = snake_logo_resized.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Rysowanie logo i tekstu na ekranie
    screen.blit(text, (100, 10))
    screen.blit(snake_logo_resized, logo_rect)

    # Aktualizacja ekranu
    pygame.display.flip()

    # Zwracanie wyboru
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    return EASY
                elif event.key == pygame.K_m:
                    return MEDIUM
                elif event.key == pygame.K_h:
                    return HARD


# Główna pętla gry
def main():
    # Ustawienie poziomu trudności
    difficulty = select_difficulty()
    global FPS, APPLE_DURATION
    FPS = difficulty["FPS"]
    APPLE_DURATION = difficulty["APPLE_DURATION"]

    # Wyświetlenie ekranu startowego
    start_screen()

    # Inicjalizacja początkowych obiektów gry
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = RIGHT
    apple = generate_apple(snake)
    poison_apple = generate_poison_apple(snake)
    apple_duration_counter = APPLE_DURATION

    score = 0
    move = True

    # Pętla zmian kierunków poruszania się węża
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause_game(score)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN and move:
                    direction = UP
                    move = False
                elif event.key == pygame.K_DOWN and direction != UP and move:
                    direction = DOWN
                    move = False
                elif event.key == pygame.K_LEFT and direction != RIGHT and move:
                    direction = LEFT
                    move = False
                elif event.key == pygame.K_RIGHT and direction != LEFT and move:
                    direction = RIGHT
                    move = False
                elif event.key == pygame.K_SPACE:
                    pause_game(score)

        if move_snake(snake, direction, grow_tail=False):
            move = True

        # Sprawdzenie kolizji z jabłkiem
        if snake[0] == apple:
            score += 1
            move_snake(snake, direction, grow_tail=True)  # Wydłuż węża
            apple_duration_counter = APPLE_DURATION  # Reset czasu trwania jabłka
            apple = generate_apple(snake)  # Generowanie kolejnego jabłka

        # Sprawdzenie kolizji z niebieskim jabłkiem
        if snake[0] == poison_apple:
            if score == 0:
                print("Game Over! Your score:", score)
                pygame.quit()
                sys.exit()
            else:
                score -= 1
            snake.pop()  # Skróć węża
            poison_apple = generate_poison_apple(snake)  # Generowanie kolejnego zatrutego jabłka

        # Sprawdzenie kolizji z samym sobą
        if snake[0] in snake[1:]:
            print("Game Over! Your score:", score)
            save_score_with_nick(score)  # Możliwość zapisania wyniku
            display_score(score)  # Wyświetlenie wyniku na ekranie startowym
            pygame.quit()
            sys.exit()

        # Sprawdzenie periodycznych warunków brzegowych
        # Pozycja głowy węża jest po zastosowaniu operatora modulo
        # przenoszona na driugi koniec ekranu
        snake[0] = (snake[0][0] % WIDTH, snake[0][1] % HEIGHT)

        # Rysowanie na ekranie
        screen.fill(WHITE)                  # Wypełnienie tła na biało
        draw_snake(snake)                   # Rysowanie węża
        draw_apple(apple)                   # Rysowanie jabłka
        draw_poison_apple(poison_apple)     # Rysowanie zatrutego jabłka
        display_current_score(score)        # Wyświetlanie aktualnego wyniku
        pygame.display.flip()               # Aktualizacja ekranu gry

        # Zmniejszanie czasu trwania jabłka
        if apple_duration_counter > 0:
            apple_duration_counter -= 1
        else:
            apple = generate_apple(snake)  # Rysowanie nowego jabłka
            poison_apple = generate_poison_apple(snake)  # Rysowanie nowego zatrutego jabłka
            apple_duration_counter = APPLE_DURATION  # Reset czasu trwania jabłek

        pygame.display.flip()  # Aktualizacja ekranu gry
        clock.tick(FPS)  # Funkcja kontrolująca liczbę klatek na sekundę


# Sprawdzenie bezpośredniego wywołania funkcji main
if __name__ == "__main__":
    main()

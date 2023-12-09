import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Ustawienia gry
WIDTH, HEIGHT = 800, 600
FPS = 10
BLOCK_SIZE = 20
SNAKE_SPEED = 20
APPLE_DURATION = 100  # Ilość klatek, przez które jabłko będzie widoczne
APPLE_POINTS = 10
POISON_POINTS_PENALTY = 5

# Kolory
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))


def draw_apple(apple):
    pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], BLOCK_SIZE, BLOCK_SIZE))


def draw_poison_apple(poison_apple):
    pygame.draw.rect(screen, BLUE, pygame.Rect(poison_apple[0], poison_apple[1], BLOCK_SIZE, BLOCK_SIZE))


def move_snake(snake, direction, grow_tail=False):
    new_head = (snake[0][0] + direction[0] * BLOCK_SIZE, snake[0][1] + direction[1] * BLOCK_SIZE)
    snake.insert(0, new_head)
    if not grow_tail:
        snake.pop()


def generate_apple(snake):
    while True:
        apple = (random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                 random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
        if apple not in snake:
            return apple


def generate_poison_apple(snake):
    while True:
        poison_apple = (random.randrange(0, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                        random.randrange(0, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE)
        if poison_apple not in snake:
            return poison_apple


def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = RIGHT
    apple = generate_apple(snake)
    poison_apple = generate_poison_apple(snake)
    apple_duration_counter = APPLE_DURATION
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        move_snake(snake, direction, grow_tail=False)

        # Sprawdzenie kolizji z jabłkiem
        if snake[0] == apple:
            score += 1
            move_snake(snake, direction, grow_tail=True)  # Wydłuż węża
            apple = generate_apple(snake)

        # Sprawdzenie kolizji z niebieskim jabłkiem
        if snake[0] == poison_apple:
            score -= 1
            snake.pop()  # Skróć węża
            poison_apple = generate_poison_apple(snake)

        # Sprawdzenie kolizji z samym sobą
        if snake[0] in snake[1:]:
            print("Game Over! Your score:", score)
            pygame.quit()
            sys.exit()

        # Sprawdzenie periodycznych warunków brzegowych
        snake[0] = (snake[0][0] % WIDTH, snake[0][1] % HEIGHT)

        # Rysowanie na ekranie
        screen.fill(WHITE)
        draw_snake(snake)
        draw_apple(apple)
        draw_poison_apple(poison_apple)

        # Zmniejsz czas trwania jabłka
        if apple_duration_counter > 0:
            apple_duration_counter -= 1
        else:
            apple = generate_apple(snake)
            apple_duration_counter = APPLE_DURATION

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

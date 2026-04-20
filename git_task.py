import pygame
import random

# Initializare Pygame
pygame.init()

# Constante
WINDOW_SIZE = 500
GRID_SIZE = 10
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
REGEN_TIME = 5000  # milisecunde (5 secunde)

# Creare fereastra
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Procedural Color Grid (Press SPACE to Regenerate)")

# Functie care genereaza o matrice de culori random
def generate_color_grid():
    return [
        [
            (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            for _ in range(GRID_SIZE)
        ]
        for _ in range(GRID_SIZE)
    ]

# Functie care deseneaza grid-ul pe ecran
def draw_grid(surface, color_grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, color_grid[row][col], rect)

# Initializare date
color_grid = generate_color_grid()
last_update_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill((0, 0, 0))

    # Desenare grid
    draw_grid(screen, color_grid)

    pygame.display.flip()

    # Verifica daca au trecut 5 secunde
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time >= REGEN_TIME:
        color_grid = generate_color_grid()
        last_update_time = current_time

    # Gestionare evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Regenerare manuala la apasarea tastei SPACE
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color_grid = generate_color_grid()
            last_update_time = pygame.time.get_ticks()

pygame.quit()
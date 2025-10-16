import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Stars")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Player settings
player_width = 80
player_height = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Star settings
star_radius = 10
stars = []

# Clock for FPS
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.SysFont("comicsans", 30)

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS
    win.fill(BLACK)

    # Spawn stars randomly
    if random.randint(1, 20) == 1:
        stars.append([random.randint(0, WIDTH - star_radius), 0])

    # Move stars
    for star in stars:
        star[1] += 5
        pygame.draw.circle(win, YELLOW, star, star_radius)

    # Remove stars that fall off screen
    stars = [star for star in stars if star[1] < HEIGHT]

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Draw player
    pygame.draw.rect(win, RED, (player_x, player_y, player_width, player_height))

    # Check collision with stars
    for star in stars:
        if player_y < star[1] + star_radius < player_y + player_height and \
           player_x < star[0] < player_x + player_width:
            score += 1
            stars.remove(star)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

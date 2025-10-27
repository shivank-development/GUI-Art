import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bounce Game - CLCoding")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock for FPS
clock = pygame.time.Clock()

# Paddle setup
paddle_width = 120
paddle_height = 15
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
paddle_speed = 8

# Ball setup
ball_radius = 12
ball_x = random.randint(50, WIDTH - 50)
ball_y = HEIGHT // 2
ball_dx = 5
ball_dy = -5

# Score
score = 0
font = pygame.font.SysFont("Arial", 28, bold=True)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collisions (walls)
    if ball_x <= 0 or ball_x >= WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    # Ball hits paddle
    if (paddle_y - ball_radius < ball_y < paddle_y) and (paddle_x < ball_x < paddle_x + paddle_width):
        ball_dy = -ball_dy
        score += 1

    # Ball missed (game over)
    if ball_y > HEIGHT:
        game_over_text = font.render("GAME OVER! Press R to Restart or Q to Quit", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 300, HEIGHT // 2))
        pygame.display.update()

        # Wait for restart or quit
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset game
                        ball_x = random.randint(50, WIDTH - 50)
                        ball_y = HEIGHT // 2
                        ball_dx, ball_dy = 5, -5
                        score = 0
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    # Draw paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, BLACK, (ball_x, ball_y), ball_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)  # FPS

import pygame
import math

pygame.init()

# Screen
s = pygame.display.set_mode((600, 400))
c = pygame.time.Clock()

# Pendulum properties
origin = (300, 50)
L = 200               # Length of pendulum
a = math.pi / 4       # Initial angle
av = 0                # Angular velocity
g = 0.5               # Gravity

run = True
while run:
    s.fill((0, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    # Physics: angular acceleration (θ'' = -g/L * sinθ)
    aa = -(g / L) * math.sin(a)
    av += aa
    a += av
    av *= 0.99  # damping

    # Bob position
    bob = (
        int(origin[0] + L * math.sin(a)),
        int(origin[1] + L * math.cos(a))
    )

    # Draw pendulum
    pygame.draw.line(s, (0, 255, 255), origin, bob, 3)
    pygame.draw.circle(s, (255, 0, 0), bob, 20)

    pygame.display.flip()
    c.tick(60)

pygame.quit()

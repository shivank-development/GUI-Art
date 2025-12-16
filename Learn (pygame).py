"""
pygame ek Python library hai jo:

Graphics (2D shapes, images)

Sound effects aur music

Keyboard/mouse events

Game loops
handle karne ke liye use hoti hai.

"""

#pip install pygame

#python -m pygame.examples.aliens



"""import pygame
import sys

# Initialize pygame
pygame.init()

# Window size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Title
pygame.display.set_caption("bgmi")

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Background color
    screen.fill((255, 255, 255))  # White
    pygame.display.update()"""


# Shapes Draw Karna
"""import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Draw Shapes")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))  # Dark background

    # Draw a rectangle (surface, color, [x, y, width, height])
    pygame.draw.rect(screen, (0, 255, 0), [5, 10, 100, 60])

    # Draw a circle (surface, color, position (x, y), radius)
    pygame.draw.circle(screen, (255, 0, 0), (550, 50), 50)

    # Draw a line
    pygame.draw.line(screen, (0, 0, 255), (100, 100), (400, 300), 5)
    pygame.draw.line(screen, (0, 0, 255), (650, 650), (400, 300), 5)

    pygame.display.update()"""

# Keyboard Movement Example
"""import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Move the Ball")

x, y = 300, 200
radius = 20
speed = 0.1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)
    pygame.display.update()"""


# Sound aur Music Add Karna
"""import pygame
pygame.init()
pygame.mixer.music.load("C:\\Users\\offic\\Desktop\\The_Universe\\JARVIS_2\\alert.mp3")  # file same folder me ho
pygame.mixer.music.play(-1)  # loop forever
#pygame.mixer.music.set_volume(0.7)  # volume 0 to 1"""



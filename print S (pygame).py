import pygame

pygame.init()

# Window size
width, height = 400, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Star Letter S")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ASCII-art S
s_art = [
    " ***** ",
    "*      ",
    "*      ",
    " ***** ",
    "      *",
    "*     *",
    " ***** "
]

# Font
font = pygame.font.SysFont("Courier", 40)

running = True
while running:
    win.fill(BLACK)
    
    for i, line in enumerate(s_art):
        text = font.render(line, True, WHITE)
        win.blit(text, (50, 50 + i * 45))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

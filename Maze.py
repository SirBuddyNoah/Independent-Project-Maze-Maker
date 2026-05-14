
import pygame
import sys

pygame.init()

Width = 800
Height = 800

Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Maze-Maker 1")
clock = pygame.time.Clock()

Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    Screen.fill((30, 30, 30))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()


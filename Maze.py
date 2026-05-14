
import pygame
import sys



#Display Settings
Width = 800
Height = 800

Rows = 16
Columbs = 16

Background_Colour = (30, 30, 30)
Grid_Colour = (0, 0, 0)

Cell_Width = Width // Columbs
Cell_Height = Height // Rows

#Pygame Setup
pygame.init()
Screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Maze-Maker 1")
clock = pygame.time.Clock()

#Grid construct
def draw_grid():
    for row in range(Rows):
        for col in range(Columbs):
            x = col * Cell_Height
            y = row * Cell_Width

            rectangle = pygame.Rect(
                x,
                y,
                Cell_Width,
                Cell_Height
            )
            pygame.draw.rect(
                Screen,
                Grid_Colour,
                rectangle,
                1
            )

#Game Loop
Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    Screen.fill(Background_Colour)
    draw_grid()
    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()

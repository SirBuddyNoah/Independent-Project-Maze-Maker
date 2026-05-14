
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

#Cells

class Cell:

    def __init__(self, row, col):

        self.row = row
        self.col = col

        self.visited = False

        self.walls = {

            "Up": True,

            "Down": True,

            "Left": True,

            "Right": True

        }

#Grid
Grid = []
for row in range(Rows):

    Grid_row = []

    for col in range(Columbs):

        cell = Cell(row, col)

        Grid_row.append(cell)

    Grid.append(Grid_row)
#Grid construct

def draw_grid():

    for row in Grid:

        for cell in row:

            x = cell.col * Cell_Height
            y = cell.row * Cell_Width


            #Up
            if cell.walls["Up"]:
                pygame.draw.line(
                    Screen,
                    Grid_Colour,
                    (x,y),
                    (x + Cell_Width, y),
                    2
                )
               
            #Down
            #Left
            #Right


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

import pygame
import sys
import random


SC_WDTH = 480
SC_HGHT = 480

GRIDSIZE = 20

GRID_WDTH = SC_HGHT / GRIDSIZE
GRID_HGHT = SC_WDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class snake(object):

    def __init__(self):
        pass

    def get_pos(self):
        pass

    def turn(self,point):
        pass

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self,surface):
        pass
    
    def control(self):
        pass


class food(object):

    def __init__(self):
        pass

    def rand_pos(self):
        pass

    def draw(self, surface):
        pass



def genGrid(Surface):
    for y in range(0,int(GRID_HGHT)):
        for x in range (0, int(GRID_WDTH)):
            if ( y + x) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface,(93, 216, 228), r)

            else:
                r_b = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(surface,(84,194, 205), r_b)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SC_WDTH, SC_HGHT),0,32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    genGrid(surface)

    score = 0
    while (True):
        clock.tick(10)

        screen.blit(surface, (0,0))
        pygame.display.update()

main()
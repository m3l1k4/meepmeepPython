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

        self.length = 1
        self.positions = [((SC_WDTH/2),(SC_HGHT/2))]
        self.direction = random.choice([UP,DOWN,LEFT, RIGHT])
        self.color = (13, 24, 50)
 

    def get_pos(self):
        return self.positions[0]

    def turn(self,point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return 
        else: 
            self.direction = point

    def move(self):
        currentPos= self.get_pos()
        x,y = self.direction
        new = (((currentPos[0] + (x*GRIDSIZE))% SC_WDTH),(currentPos[1] +(y*GRIDSIZE)) % SC_HGHT)
        if len(self.positions)>2 and new in self.positions[2:]:
            self.reset()
        
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()
       

    def reset(self):
        self.length = 1
        self.positions = [((SC_WDTH/2), (SC_HGHT/2))]
        self.direction = random.choice((UP, DOWN,LEFT,RIGHT))

    def draw(self,Surface):
        for p in self.positions:
            x= pygame.rect((p[0], p[1], (GRIDSIZE, GRIDSIZE)))
            pygame.draw.rect(Surface, self.color,x)
            pygame.draw.rect(Surface,(93,216,228),r,1)
            
    
    def control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class food(object):

    def __init__(self):
        pass

    def rand_pos(self):
        pass

    def draw(self, Surface):
        pass



def genGrid(Surface):
    for y in range(0,int(GRID_HGHT)):
        for x in range (0, int(GRID_WDTH)):
            if ( y + x) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(Surface,(93, 216, 228), r)

            else:
                r_b = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),(GRIDSIZE,GRIDSIZE))
                pygame.draw.rect(Surface,(84,194, 205), r_b)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SC_WDTH, SC_HGHT),0,32)

    Surface = pygame.Surface(screen.get_size())
    Surface = Surface.convert()

    genGrid(Surface)

    score = 0
    while (True):
        clock.tick(10)

        screen.blit(Surface, (0,0))
        pygame.display.update()

main()
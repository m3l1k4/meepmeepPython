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


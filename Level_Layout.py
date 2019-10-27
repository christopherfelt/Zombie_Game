import pygame

class Wall(object):

    walls = []

    def __init__(self, pos):

        Wall.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)


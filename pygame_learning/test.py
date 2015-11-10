import pygame

pygame.init()

class Spielfeld(object):

    def __init__(self):
        self.graphics = self.load_graphic()
        print self.graphics[0]

    def load_graphic(self):
        list_of_gfx = []
        left_top_corner = pygame.image.load('tilesets/trockener boden auf gras/001.bmp')
        list_of_gfx.append(left_top_corner)
        top_border = pygame.image.load('tilesets/trockener boden auf gras/002.bmp')
        list_of_gfx.append(top_border)
        monster = pygame.image.load('characters/monster.png')
        list_of_gfx.append(monster)
        croco = pygame.image.load('characters/croco.png')
        list_of_gfx.append(croco)
        return list_of_gfx

spielfeld = Spielfeld()
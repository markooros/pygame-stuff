import pygame
import pygame.locals

class TileLoader(object):

    def __init__(self, filename, width, height):
        self.filename = filename
        self.width = width
        self.height = height


    def load_tile_table(self):
        image = pygame.image.load(self.filename).convert()
        image_width, image_height = image.get_size()
        tile_table = []
        for tile_x in range(0, image_width/self.width):
            line = []
            tile_table.append(line)
            for tile_y in range(0, image_height/self.height):
                rect = (tile_x*self.width, tile_y*self.height, self.width, self.height)
                line.append(image.subsurface(rect))
        return tile_table

if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((128, 98))
    screen.fill((255, 255, 255))
    loader = TileLoader("tileset/basic_tileset.png", 24, 16)
    table = loader.load_tile_table()
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*32, y*24))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
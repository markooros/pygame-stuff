import sys
import pygame
from pygame.locals import *
import random


class Hero(pygame.sprite.Sprite):

    def __init__(self,screen):

        super(Hero, self).__init__()

        self.screen = screen

        self.img = pygame.image.load('characters/hero.png')

        self.init_position = (512,512)

        self.position = self.init_position

    def update(self,time_passed):
        if time_passed < 20:
            pygame.display.update()
        return

    def draw(self):
        self.screen.blit(self.img, self.init_position)

BG_COLOR = 150, 150, 80

pygame.init()
screen = pygame.display.set_mode((1024, 1024), 0, 32)
clock = pygame.time.Clock()

hero = []
hero.append(Hero(screen))
step = 0

while True:
    time_passed = clock.tick(50)
    for event in pygame.event.get():
        pygame.display.flip()
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and step == 0:
            screen.fill(BG_COLOR)
            step += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and step == 1:
            for i in hero:
                i.update(time_passed)
                i.draw()
            pygame.display.flip()


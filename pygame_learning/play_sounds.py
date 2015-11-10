import pygame

pygame.init()

soundObj = pygame.mixer.Sound('sounds/beeps.wav')
pygame.mixer.music.load('sounds/background.mp3')

pygame.mixer.music.play(-1, 0.0)

import time

time.sleep(60)

pygame.mixer.music.stop()
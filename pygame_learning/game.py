import pygame
import sys
from random import randint
from pygame.locals import *

from learn_rpg.text_based.modules.Character import *
from text_based.modules.Monster import *
from text_based.modules.Maps import *


class Game(object):

    def __init__(self):
        pygame.init()
        self.graphics = self.load_graphic()
        self.tileset = self.define_tileset()
        self.stone_locations = {}
        self.hero_location = {}
        self.monsters = {}
        self.monsters_inital_locations = []
        self.black = (  0,   0,   0)
        self.DISPLAYSURF = pygame.display.set_mode((1024, 1024))
        self.my_hero = self.init_hero()
        self.my_map = self.init_map_data()
        self.run_game()

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
        filler = pygame.image.load('tilesets/variationen/007.bmp')
        list_of_gfx.append(filler)
        stone = pygame.image.load('tilesets/variationen/001.bmp')
        list_of_gfx.append(stone)
        hero = pygame.image.load('characters/hero.png')
        list_of_gfx.append(hero)
        return list_of_gfx


    def define_tileset(self):
        tileset = {'top_border': self.graphics[1],
                   'left_side': pygame.transform.rotate(self.graphics[1], 90),
                   'right_side': pygame.transform.rotate(self.graphics[1], 270),
                   'bottom_border': pygame.transform.rotate(self.graphics[1], 180),
                   'left_top_corner': self.graphics[0],
                   'right_top_corner': pygame.transform.rotate(self.graphics[0], 270),
                   'right_bottom_corner': pygame.transform.rotate(self.graphics[0], 180),
                   'left_bottom_corner': pygame.transform.rotate(self.graphics[0], 90),
                   'filler': self.graphics[4],
                   'stone': self.graphics[5]
                    }
        return tileset

    def create_random_coordinate(self):
        rnd_coordinate = randrange(64,896,64)
        return rnd_coordinate

    def draw_playfield(self):
        number = 0
        for x in range(0,960,64):
            for y in range(64,960,64):
                randomize = randint(0, 10)
                if randomize >= 2:
                    self.DISPLAYSURF.blit(self.tileset.get('filler'),(x,y))
                else:
                    self.DISPLAYSURF.blit(self.tileset.get('stone'),(x,y))
                    self.stone_locations['stones{0}'.format(number)] = (x,y)
                    number += 1
            self.DISPLAYSURF.blit(self.tileset.get('top_border'),(x,0))
            self.DISPLAYSURF.blit(self.tileset.get('left_side'),(0,x))
            self.DISPLAYSURF.blit(self.tileset.get('right_side'),(960,x))
            self.DISPLAYSURF.blit(self.tileset.get('bottom_border'),(x,960))
            self.DISPLAYSURF.blit(self.tileset.get('left_top_corner'),(0,0))
            self.DISPLAYSURF.blit(self.tileset.get('left_bottom_corner'),(0,960))
            self.DISPLAYSURF.blit(self.tileset.get('right_top_corner'),(960,0))
            self.DISPLAYSURF.blit(self.tileset.get('right_bottom_corner'),(960,960))

        pygame.display.set_caption('Hello World!')
        return self.stone_locations

    def add_monsters(self, expected_number_of_monsters):
        number = expected_number_of_monsters
        while number > 0:
            coordinates = {}
            monster_placement = self.get_list_of_initial_monster_placement()
            random_x = self.create_random_coordinate()
            random_y = self.create_random_coordinate()
            if (random_x,random_y) not in self.stone_locations \
                    and (random_x,random_y) not in monster_placement\
                    and random_x != self.hero_location['x']\
                    and random_y != self.hero_location['y']:
                self.DISPLAYSURF.blit(self.graphics[3],(random_x,random_y))
                coordinates['x'] = random_x
                coordinates['y'] = random_y
                self.monsters["monster{0}".format(number)]=Monster(self.my_map.get_map_monster_lvl_range(),self.my_hero.get_hero_lvl(), coordinates)
                number -= 1
        return self.monsters

    def get_list_of_initial_monster_placement(self):
        for monster in self.monsters.keys():
            monster = self.monsters[monster]
            location = monster.get_monster_location()
            x = location['x']
            y = location['y']
            self.monsters_inital_locations.append((x,y))
        return self.monsters_inital_locations

    def get_monster_data(self, monster_id):
        return self.monsters[monster_id]

    def spawn_hero(self):
        hero_spawned = False
        while hero_spawned is False:
            random_x = self.create_random_coordinate()
            random_y = self.create_random_coordinate()
            if (random_x,random_y) not in self.stone_locations.values():
                self.DISPLAYSURF.blit(self.graphics[6],(random_x,random_y))
                self.hero_location['x'] = random_x
                self.hero_location['y'] = random_y
                hero_spawned = True
        return self.hero_location

    def check_hero_movement(self,direction):
        coords = self.hero_location

        if coords['x'] in range(64,960,64) and coords['y'] in range(64,960,64):
            if direction == 'left' and\
            (int(coords['x']-64),int(coords['y'])) not in self.stone_locations.values():
                self.DISPLAYSURF.blit(self.graphics[6],(coords['x'],coords['y']))
                self.DISPLAYSURF.blit(self.graphics[4],(int(coords['x']+64),coords['y']))
                pygame.display.update()
                return True
            elif direction == 'right' and\
            (int(coords['x']+64),int(coords['y'])) not in self.stone_locations.values():
                self.DISPLAYSURF.blit(self.graphics[6],(coords['x'],coords['y']))
                self.DISPLAYSURF.blit(self.graphics[4],(int(coords['x']-64),coords['y']))
                pygame.display.update()
                return True
            elif direction == 'up' and\
            (int(coords['x']),int(coords['y']-64)) not in self.stone_locations.values():
                self.DISPLAYSURF.blit(self.graphics[6],(coords['x'],coords['y']))
                self.DISPLAYSURF.blit(self.graphics[4],(coords['x'],int(coords['y']+64)))
                pygame.display.update()
                return True
            elif direction == 'down' and\
            (int(coords['x']),int(coords['y']+64)) not in self.stone_locations.values():
                self.DISPLAYSURF.blit(self.graphics[6],(coords['x'],coords['y']))
                self.DISPLAYSURF.blit(self.graphics[4],(coords['x'],int(coords['y']-64)))
                pygame.display.update()
                return True
        else:
            pygame.display.update()
            return False

    def draw_main_menu(self): #draw main menu normally
        self.DISPLAYSURF.fill(self.black) #clears screen
        font = pygame.font.Font(None, 16)
        new_text = font.render('NEW GAME', 1, (100, 100, 100))
        load_text = font.render('LOAD GAME', 1, (100, 100, 100))
        options_text = font.render('OPTIONS', 1, (100, 100, 100))
        quit_text = font.render('QUIT', 1,  (100, 100, 100))

        self.DISPLAYSURF.blit(new_text, (340, 425))
        self.DISPLAYSURF.blit(load_text, (335, 455))
        self.DISPLAYSURF.blit(options_text, (350, 485))
        self.DISPLAYSURF.blit(quit_text, (373, 515))
        pygame.display.update()

    def run_game(self):
        once = 0
        self.draw_main_menu()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] in range(400,450,1) and once == 0:
                        self.start_new_game()
                        once += 1
                elif event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        print "move down"
                        if self.check_hero_movement('down') is True:
                            self.my_hero.move_down()
                    elif event.key == K_UP:
                        print "move up"
                        if self.check_hero_movement('up') is True:
                            self.my_hero.move_up()
                    elif event.key == K_LEFT:
                        print "move left"
                        if self.check_hero_movement('left') is True:
                            self.my_hero.move_left()
                    elif event.key == K_RIGHT:
                        print "move right"
                        if self.check_hero_movement('right') is True:
                            self.my_hero.move_right()

    def init_hero(self):
        my_hero = self.choose_character_class()
        return my_hero

    def choose_character_class(self):

        char_class_choice = raw_input("Choose your Class(Warrior, Rogue, Mage): ")
        print "You choose to be a " + char_class_choice

        if char_class_choice.upper() == "WARRIOR":
            my_hero = Warrior(self.hero_location)
            my_hero.add_base_stats()
            return my_hero
        elif char_class_choice.upper() == "MAGE":
            my_hero = Mage(self.hero_location)
            my_hero.add_base_stats()
            return my_hero
        elif char_class_choice.upper() == "ROGUE":
            my_hero = Rogue(self.hero_location)
            my_hero.add_base_stats()
            return my_hero
        else:
            print "WHAT ????"
            exit('unable to process your choice')

    def init_map_data(self):
        my_map = Map(self.my_hero.get_hero_lvl())
        return my_map

    def start_new_game(self):
        self.draw_playfield()
        self.spawn_hero()
        self.add_monsters(10)
        pygame.display.update()



my_game = Game()
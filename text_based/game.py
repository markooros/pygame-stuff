import pygame
import sys
from pygame.locals import *

from modules.Character import *
from modules.Monster import Monster
from modules.Maps import Map
from modules.Drawing import DrawingParameters
from modules.Fight import Fight


class Game(object):
    def __init__(self):
        pygame.init()
        self.drawing_parameters = DrawingParameters()
        self.colors = self.drawing_parameters.get_colors()
        self.DISPLAYSURF = pygame.display.set_mode((512, 512))
        self.small_font = pygame.font.Font(None, 16)
        self.big_font = pygame.font.Font(None, 24)
        self.dimension = 512
        self.color = self.colors['grey']
        self.run_game()

    def clear_screen(self):
        self.DISPLAYSURF.fill(self.colors['black'])
        pygame.display.update()

    def goodbye(self):
        self.clear_screen()
        goodbye = self.big_font.render('GOODBYE', 1, self.color)
        self.DISPLAYSURF.blit(goodbye, (self.dimension - 300, self.dimension - 300))
        pygame.display.update()
        pygame.time.delay(2000)
        exit(0)

    def draw_start_menu(self):
        self.clear_screen()

        new_text = self.small_font.render('NEW GAME', 1, self.color)
        options_text = self.small_font.render('OPTIONS', 1, self.color)
        quit_text = self.small_font.render('QUIT', 1, self.color)

        self.DISPLAYSURF.blit(new_text, (self.dimension - 300, self.dimension - 300))
        self.DISPLAYSURF.blit(options_text, (self.dimension - 300, self.dimension - 275))
        self.DISPLAYSURF.blit(quit_text, (self.dimension - 300, self.dimension - 250))
        pygame.display.update()

    def draw_fight_question(self):
        fight_question = self.small_font.render('WANNA FIGHT ?', 1, self.color)
        selection_text = self.small_font.render('YES / NO', 1, self.color)

        self.DISPLAYSURF.blit(fight_question, (self.dimension - 335, self.dimension - 200))
        self.DISPLAYSURF.blit(selection_text, (self.dimension - 322, self.dimension - 175))

    def draw_character_info(self):
        position = self.dimension - 490
        for line in str(self.my_hero).split('\n'):
            rendered_line = self.big_font.render(line, 1, self.color)
            self.DISPLAYSURF.blit(rendered_line, (self.dimension - 500, position))
            position += 25

    def draw_monster_info(self, monster):
        position = self.dimension - 490
        for line in str(monster).split('\n'):
            rendered_line = self.big_font.render(line, 1, self.color)
            self.DISPLAYSURF.blit(rendered_line, (self.dimension - 200, position))
            position += 25
        self.draw_fight_question()

    def draw_encounter(self, monster):
        self.clear_screen()
        self.draw_character_info()
        self.draw_monster_info(monster)
        self.draw_fight_question()
        pygame.display.update()

    def draw_character_class_selection(self):
        self.clear_screen()
        position = self.dimension
        classes = {'Warrior', 'Rogue', 'Mage'}
        class_question = self.big_font.render('What type of hero would you like to be?', 1, self.color)
        self.DISPLAYSURF.blit(class_question, (self.dimension - 400, position - 450))
        for item in classes:
            rendered_line = self.big_font.render(item, 1, self.color)
            self.DISPLAYSURF.blit(rendered_line, (self.dimension - 400, position - 400))
            position += 25
        pygame.display.update()

    def draw_color_sheme_selection(self):
        self.clear_screen()
        position = self.dimension
        colors = {'RED', 'BLUE', 'GREEN'}
        color_question = self.big_font.render('Which color would you like?', 1, self.color)
        self.DISPLAYSURF.blit(color_question, (self.dimension - 400, position - 450))
        for item in colors:
            rendered_line = self.big_font.render(item, 1, self.color)
            self.DISPLAYSURF.blit(rendered_line, (self.dimension - 400, position - 400))
            position += 25
        pygame.display.update()

    def fighting(self, my_hero):
        self.clear_screen()
        my_map = Map(my_hero.get_hero_lvl())
        my_monster = Monster(my_map.get_map_monster_lvl_range(), my_hero.get_hero_lvl())
        start_fight = self.big_font.render('=== Start Fight ===', 1, self.color)
        self.DISPLAYSURF.blit(start_fight, (self.dimension - 350, self.dimension - 350))
        pygame.display.update()
        fight = Fight(my_hero, my_monster)
        fight.fighting(my_hero.get_hero_hp(), my_monster.get_monster_hp())
        fight_log = fight.get_fight_log()
        position = self.dimension - 300
        stop = False
        while stop is False:
            for line in fight_log:
                if position <= 450:
                    rendered_line = self.big_font.render(line, 1, self.color)
                    self.DISPLAYSURF.blit(rendered_line, (self.dimension - 350, position))
                    position += 25
                    pygame.display.update()
                    if fight_log.index(line) == len(fight_log) - 1:
                        stop = True
                else:
                    pygame.time.delay(1000)
                    self.clear_screen()
                    position = self.dimension - 300
                    rendered_line = self.big_font.render(line, 1, self.color)
                    self.DISPLAYSURF.blit(rendered_line, (self.dimension - 350, position))
                    position += 25
                    pygame.display.update()
                    if fight_log.index(line) == len(fight_log) - 1:
                        stop = True

        if fight is False:
            self.hero_died()

    @staticmethod
    def choose_character_class(hero_class):
        if hero_class == "WARRIOR":
            my_hero = Warrior()
            my_hero.add_base_stats()
            return my_hero
        elif hero_class == "MAGE":
            my_hero = Mage()
            my_hero.add_base_stats()
            return my_hero
        elif hero_class == "ROGUE":
            my_hero = Rogue()
            my_hero.add_base_stats()
            return my_hero
        else:
            print "WHAT ????"
            exit('unable to process your choice')

    def choose_color_sheme(self, color_choice):
        if color_choice == "RED":
            self.color = self.colors['red']
        elif color_choice == "BLUE":
            self.color = self.colors['blue']
        elif color_choice == "GREEN":
            self.color = self.colors['green']

    def spawn_monster(self):
        my_map = Map(self.my_hero.get_hero_lvl())
        my_monster = Monster(my_map.get_map_monster_lvl_range(), self.my_hero.get_hero_lvl())
        return my_monster

    def run_game(self):
        self.draw_start_menu()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] in range(190, 230, 1):
                        self.start_new_game()
                    elif mouse_pos[1] in range(235, 250, 1):
                        self.color_sheme_selection()
                    elif mouse_pos[1] in range(255, 270, 1):
                        self.goodbye()

    def color_sheme_selection(self):
        self.draw_color_sheme_selection()
        once = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] in range(115, 130, 1) and once == 0:
                        self.choose_color_sheme("BLUE")
                        self.run_game()
                        once += 1
                    elif mouse_pos[1] in range(140, 155, 1) and once == 0:
                        self.choose_color_sheme("GREEN")
                        self.run_game()
                        once += 1
                    elif mouse_pos[1] in range(165, 180, 1) and once == 0:
                        self.choose_color_sheme("RED")
                        self.run_game()
                        once += 1
        pygame.display.update()

    def start_new_game(self):
        self.draw_character_class_selection()
        once = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] in range(115, 130, 1) and once == 0:
                        self.my_hero = self.choose_character_class("WARRIOR")
                        self.start_encounter()
                        once += 1
                    elif mouse_pos[1] in range(140, 155, 1) and once == 0:
                        self.my_hero = self.choose_character_class("ROGUE")
                        self.start_encounter()
                        once += 1
                    elif mouse_pos[1] in range(165, 180, 1) and once == 0:
                        self.my_hero = self.choose_character_class("MAGE")
                        self.start_encounter()
                        once += 1
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.draw_character_class_selection()
                    if once == 1:
                        once -= 1
        pygame.display.update()

    def start_encounter(self):
        my_monster = self.spawn_monster()
        self.draw_character_info()
        self.draw_encounter(my_monster)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[1] in range(335, 350) and mouse_pos[0] in range(190, 210):
                        self.fighting(self.my_hero)
                        pygame.time.delay(3000)
                        self.clear_screen()
                        self.start_encounter()
                    elif mouse_pos[1] in range(335, 350) and mouse_pos[0] in range(220, 235):
                        self.clear_screen()
                        self.draw_character_info()
                        pygame.display.update()
                        pygame.time.delay(2000)
                        self.run_game()
        pygame.display.update()


my_game = Game()
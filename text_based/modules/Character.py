from random import randrange


class Character(object):
    def __init__(self):

        self.char_class = self.char_class
        self.strength = randrange(0, 5)
        self.intelligence = randrange(0, 5)
        self.luck = randrange(0, 5)
        self.hp = randrange(100, 1000, 50)
        self.mp = randrange(50, 500, 50)
        self.lvl = 1
        self.exp = 0
        self.max_lvl = 100
        # self.hero_location = hero_location

    def __repr__(self):
        return "I am a level " + str(self.lvl) + " " + str(self.char_class) + "\n" \
                                                                              "----------------" + "\n" \
                                                                                                   "strength: " + str(
            self.strength) + "\n" \
                             "intelligence: " + str(self.intelligence) + "\n" \
                                                                         "luck: " + str(self.luck) + "\n" \
                                                                                                     "hp: " + str(
            self.hp) + "\n" \
                       "mp: " + str(self.mp) + "\n" \
                                               "base attack: " + str(self.base_attack) + "\n" \
                                                                                         "current EXP: " + str(
            self.exp) + "\n"

    def determine_base_attack_factor(self):
        if self.lvl in range(10):
            self.base_attack_factor = 2
        elif self.lvl in range(10, 30):
            self.base_attack_factor = 5
        elif self.lvl in range(30, 100):
            self.base_attack_factor = 10
        return self.base_attack_factor

    def determine_main_stat(self):
        if self.char_class is "Mage":
            self.main_stat = self.intelligence
        elif self.char_class is "Warrior":
            self.main_stat = self.strength
        elif self.char_class is "Rogue":
            self.main_stat = self.luck
        return self.main_stat

    def determine_base_attack(self):
        self.base_attack = self.determine_main_stat() * self.lvl / self.determine_base_attack_factor()
        return self.base_attack


    def basic_attack(self, monster_hp):

        fighting_monster_hp = monster_hp
        while fighting_monster_hp > 0:
            fighting_monster_hp = fighting_monster_hp - self.base_attack
            print "Monster got " + str(fighting_monster_hp) + " HP left"

        return True

    def get_hero_hp(self):
        return self.hp

    def get_hero_lvl(self):
        return self.lvl

    def get_hero_location(self):
        return self.hero_location

    def move_left(self):
        current_location = self.get_hero_location()
        current_location['x'] = int(current_location['x'] - 64)
        self.hero_location = current_location
        return self.hero_location

    def move_right(self):
        current_location = self.get_hero_location()
        current_location['x'] = int(current_location['x'] + 64)
        self.hero_location = current_location
        return self.hero_location

    def move_up(self):
        current_location = self.get_hero_location()
        current_location['y'] = int(current_location['y'] - 64)
        self.hero_location = current_location
        return self.hero_location

    def move_down(self):
        current_location = self.get_hero_location()
        current_location['y'] = int(current_location['y'] + 64)
        self.hero_location = current_location
        return self.hero_location


class Warrior(Character):
    char_class = "Warrior"

    def add_base_stats(self):
        self.strength = self.strength + 2
        self.intelligence = self.intelligence + 1
        self.luck = self.luck + 1
        self.hp = self.hp + 50
        self.mp = self.mp + 2
        self.base_attack = self.determine_base_attack()

    def lvl_up(self, number_of_lvls):
        if self.lvl + number_of_lvls > self.max_lvl:
            print "max level is", self.max_lvl
        elif (self.lvl + number_of_lvls) <= self.max_lvl:
            for i in range(number_of_lvls):
                self.add_base_stats()
                self.lvl = self.lvl + 1
                self.base_attack = self.determine_base_attack()
        else:
            pass


class Mage(Character):
    char_class = "Mage"

    def add_base_stats(self):
        self.strength = self.strength + 1
        self.intelligence = self.intelligence + 2
        self.luck = self.luck + 1
        self.hp = self.hp + 20
        self.mp = self.mp + 50
        self.base_attack = self.determine_base_attack()

    def lvl_up(self, number_of_lvls):
        if self.lvl + number_of_lvls > self.max_lvl:
            print "max level is", self.max_lvl
        elif (self.lvl + number_of_lvls) <= self.max_lvl:
            for i in range(number_of_lvls):
                self.add_base_stats()
                self.lvl = self.lvl + 1
                self.base_attack = self.determine_base_attack()
        else:
            pass


class Rogue(Character):
    char_class = "Rogue"

    def add_base_stats(self):
        self.strength = self.strength + 1
        self.intelligence = self.intelligence + 1
        self.luck = self.luck + 2
        self.hp = self.hp + 35
        self.mp = self.mp + 35
        self.base_attack = self.determine_base_attack()

    def lvl_up(self, number_of_lvls):
        if self.lvl + number_of_lvls > self.max_lvl:
            print "max level is", self.max_lvl
        elif (self.lvl + number_of_lvls) <= self.max_lvl:
            for i in range(number_of_lvls):
                self.add_base_stats()
                self.lvl = self.lvl + 1
                self.base_attack = self.determine_base_attack()
        else:
            pass


from random import randrange


class Monster(object):
    def __init__(self, lvl, hero_lvl):

        self.lvl = lvl
        self.strength = self.lvl_strength_ranges()
        self.hp = self.lvl_hp_ranges()
        self.base_attack = self.determine_base_attack()
        self.exp_points = self.determine_exp_points(hero_lvl)

    def __repr__(self):
        return "I am a Level " + str(self.lvl) + " Monster" + "\n" \
                                                              "----------------" + "\n" \
                                                                                   "strength: " + str(
            self.strength) + "\n" \
                             "hp: " + str(self.hp) + "\n" \
                                                     "base attack: " + str(self.base_attack) + "\n"

    def determine_base_attack_factor(self):
        if self.lvl in range(10):
            self.base_attack_factor = 2
        elif self.lvl in range(10, 30):
            self.base_attack_factor = 5
        elif self.lvl in range(30, 200):
            self.base_attack_factor = 10
        return self.base_attack_factor

    def determine_base_attack(self):
        self.base_attack = self.strength * self.lvl / self.determine_base_attack_factor() \
                           + randrange(1, 10) - randrange(1, 10)
        if self.base_attack <= 0:
            self.determine_base_attack()
        return self.base_attack

    def determine_exp_points(self, hero_lvl):
        monster_exp_points = (self.lvl * 8) / hero_lvl
        return monster_exp_points

    def lvl_strength_ranges(self):
        if self.lvl in range(5):
            self.strength = randrange(1, 5)
        elif self.lvl in range(5, 10):
            self.strength = randrange(5, 10)
        elif self.lvl in range(10, 50):
            self.strength = randrange(10, 50)
        elif self.lvl in range(50, 200):
            self.strength = randrange(50, 100)
        return self.strength

    def lvl_hp_ranges(self):
        if self.lvl in range(5):
            self.hp = randrange(1, 5)
        elif self.lvl in range(5, 10):
            self.hp = randrange(5, 25, 5)
        elif self.lvl in range(10, 50):
            self.hp = randrange(50, 1000, 20)
        elif self.lvl in range(50, 200):
            self.hp = randrange(500, 10000, 100)
        return self.hp

    def get_monster_hp(self):
        return self.hp

    def get_monster_exp_points(self):
        return self.exp_points


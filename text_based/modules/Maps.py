from random import randrange


class Map(object):
    def __init__(self, map_lvl):

        self.map_lvl = map_lvl
        self.monster_lvl_for_map = self.define_monster_lvl_ranges_for_map()

    def __repr__(self):
        return "You are in a lvl " + str(self.map_lvl) + " Map \n" \
                                                         "A lvl " + str(
            self.monster_lvl_for_map) + " Monster spawned \n"


    def define_monster_lvl_ranges_for_map(self):
        if self.map_lvl in range(5):
            self.monster_lvl_for_map = randrange(1, 7)
        if self.map_lvl in range(5, 10):
            self.monster_lvl_for_map = randrange(6, 12)
        if self.map_lvl in range(10, 15):
            self.monster_lvl_for_map = randrange(9, 17)
        if self.map_lvl in range(15, 20):
            self.monster_lvl_for_map = randrange(14, 22)
        if self.map_lvl in range(20, 25):
            self.monster_lvl_for_map = randrange(18, 27)
        if self.map_lvl in range(25, 30):
            self.monster_lvl_for_map = randrange(23, 33)
        if self.map_lvl in range(30, 40):
            self.monster_lvl_for_map = randrange(29, 42)
        if self.map_lvl in range(40, 50):
            self.monster_lvl_for_map = randrange(38, 51)
        if self.map_lvl in range(50, 65):
            self.monster_lvl_for_map = randrange(48, 68)
        if self.map_lvl in range(65, 80):
            self.monster_lvl_for_map = randrange(62, 81)
        if self.map_lvl in range(80, 101):
            self.monster_lvl_for_map = randrange(79, 103)
        return self.monster_lvl_for_map

    def get_map_monster_lvl_range(self):
        return self.monster_lvl_for_map

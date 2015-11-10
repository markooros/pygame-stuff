class Fight(object):
    def __init__(self, hero, monster):
        self.hero_attack = hero.base_attack
        self.monster_attack = monster.base_attack
        self.hero_hp = hero.hp
        self.monster_hp = monster.hp
        self.hero = hero
        self.monster = monster
        self.fight_log = []

    def __repr__(self):
        return "hero attack " + str(self.hero_attack) + "\n" \
                                                        "monster attack " + str(self.monster_attack) + "\n" \
                                                                                                       "hero HP " + str(
            self.hero_hp) + "\n" \
                            "monster HP " + str(self.monster_hp) + "\n"

    def hero_attacks(self):

        fighting_monster_hp = self.monster_hp
        if fighting_monster_hp > 0:
            fighting_monster_hp = fighting_monster_hp - self.hero_attack
            self.fight_log.append("Monster got " + str(fighting_monster_hp) + " HP left")
        return fighting_monster_hp

    def monster_attacks(self):

        fighting_hero_hp = self.hero_hp
        if fighting_hero_hp > 0:
            fighting_hero_hp = fighting_hero_hp - self.monster_attack
            self.fight_log.append("Hero got " + str(fighting_hero_hp) + " HP left")

        return fighting_hero_hp

    def fighting(self, hero_hp, monster_hp):

        while self.monster_hp > 0:
            if self.hero_hp > 0:
                self.monster_hp = self.hero_attacks()
                self.hero_hp = self.monster_attacks()
            else:
                self.fight_log.append("Your Hero died")
                return False
        else:
            self.hero.exp = self.hero.exp + self.monster.exp_points
            self.fight_log.append("You killed the Monster")
            self.fight_log.append("you get " + str(self.monster.exp_points) + " EXP")
            if self.hero.exp >= self.hero.get_hero_lvl() * 5:
                self.hero.lvl_up(1)
                self.fight_log.append("LVL UP!")
                self.hero.exp = 0
                self.hero_hp = self.hero.get_hero_hp()

    def get_fight_log(self):
        return self.fight_log

# Standard library imports
# Local imports
from .roll import d20
from . import armor, weapons, var


# TODO: Half orc savage critical
# TODO: Fighter Action Surge
# TODO: Fighter Second Wind
# TODO: Fighter Improved Critical
# TODO: Other Racial Features
# TODO: All the barbarian stuff
# TODO: Fighting Styles
# TODO: Paladins
# TODO: Monks



class Creature:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.str = getattr(kwargs, 'str', 16)
        self.dex = getattr(kwargs, 'dex', 16)
        self.con = getattr(kwargs, 'con', 16)
        self.str_mod = self.set_ability_modifier(self.str)
        self.dex_mod = self.set_ability_modifier(self.dex)
        self.con_mod = self.set_ability_modifier(self.con)
        self.max_HP = self.set_max_HP()
        self.HP = self.max_HP
        self.features = []

    @staticmethod
    def set_ability_modifier(ability_score):
        ability_mod = (ability_score - 10)//2
        return ability_mod

    def set_max_HP(self):
        raise NotImplementedError("This method should always exist in the subclass.")

    def reset(self):
        self.HP = self.max_HP

    # Methods that a creature performs during combat:

    def roll_initiative(self):
        r = d20()
        var.output.append(f"{self.name} makes an initiative roll of [{r}+{self.dex_mod}], "
                          f"for a total of {r + self.dex_mod}.")
        return r + self.dex_mod



class Character(Creature):
    def __init__(self, **kwargs):
        self.level = int(kwargs['level'])
        self.race = kwargs['race']
        self.proficiency_bonus = self.set_proficiency_bonus()
        super().__init__(**kwargs)
        self.armor = armor.armor_dict[kwargs['armor']]
        self.weapon = weapons.weapon_dict[kwargs['weapon']]
        self.off_hand = kwargs['off_hand']
        if self.off_hand in var.weapons:
            self.off_hand_weapon = weapons.weapon_dict[self.off_hand]
        self.AC = self.set_AC()
        self.proficiency_bonus = self.set_proficiency_bonus()
        self.attack_bonus = self.set_attack_bonus()
        self.damage_bonus = self.set_damage_bonus()
        self.attacks = 1
        self.invulnerabilities = []
        self.resistances = []
        self.vulnerabilities = []
        self.uses = {}
        self.add_racial_features()

    def set_max_HP(self):
        raise NotImplementedError("This method should always exist in the subclass.")

    def set_AC(self):
        """ This method can be overriden by a subclass method where necessary"""
        armor_class = self.armor.base_AC + min(self.dex_mod, self.armor.max_dex_bonus)
        if self.off_hand == 'Shield':
            armor_class += 2
        return armor_class

    def set_proficiency_bonus(self):
        if self.level < 5:
            proficiency_bonus = 2
        elif self.level < 9:
            proficiency_bonus = 3
        elif self.level < 13:
            proficiency_bonus = 4
        elif self.level < 17:
            proficiency_bonus = 5
        else:
            proficiency_bonus = 6
        return proficiency_bonus

    def set_attack_bonus(self):
        if "Finesse" in self.weapon.properties:
            ability_mod = max(self.str_mod, self.dex_mod)
        else:
            ability_mod = self.str_mod
        if self.weapon.name in self.proficiencies:
            return ability_mod + self.proficiency_bonus
        else:
            return ability_mod

    def set_damage_bonus(self):
        if "Finesse" in self.weapon.properties:
            damage_bonus = max(self.str_mod, self.dex_mod)
        else:
            damage_bonus = self.str_mod
        return damage_bonus

    def add_racial_features(self):
        if self.race == "Half-Orc":
            self.features.append("Relentless Endurance")
            self.uses['Relentless Endurance'] = 1
            self.features.append("Savage Attacks")
        if self.race == "High Elf":
            for weapon in ["Shortsword", "Longsword", "Shortbow", "longbow"]:
                if weapon not in self.proficiencies:
                    self.proficiencies.append(weapon)
        if self.race == "Hill Dwarf":
            for weapon in ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"]:
                if weapon not in self.proficiencies:
                    self.proficiencies.append(weapon)



class Fighter(Character):
    def __init__(self, **kwargs):
        self.proficiencies = []
        self.add_weapon_proficiencies()
        super().__init__(**kwargs)
        self.fighting_style = "Duellist"
        self.add_weapon_proficiencies()

    def set_max_HP(self):
        return 10 + self.con_mod + ((4 + self.con_mod) * (self.level - 1))

    def add_weapon_proficiencies(self):
        for weapon in var.weapons:
            self.proficiencies.append(weapon)

    def __repr__(self):
        return f"""
                    {self.name} is a Level {self.level} {self.race} Fighter.
                    Max HP: {self.max_HP}
                    HP: {self.HP}
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                    Armor: {self.armor.name}
                    AC: {self.AC}
                    Weapon: {self.weapon.name}  
                """
    # TODO: Add fighting styles

    # Combat methods

    def take_turn(self, target):
        var.output.append(f"{self.name} takes their turn...")
        self.make_attack_action(target)
        if (self.off_hand in var.weapons) and (target.HP < 0):
            self.make_off_hand_attack(target)
        var.output.append(f"End of {self.name}'s turn:")
        var.output.append(f"{self.name}: {self.HP}HP")
        var.output.append(f"{target.name}: {target.HP}HP")
        var.output.append("")

    def make_attack_action(self, target):
        for _ in range(self.attacks):
            self.make_attack(target)

    def make_attack(self, target):
        var.output.append(f"{self.name} attacks {target.name} with their {self.weapon.name}.")
        attack_roll = self.make_attack_roll()
        if attack_roll == "Crit Fail":
            var.output.append(f"{self.name} rolls a 1 on their attack roll, critically failing the attack, "
                              f"and doing no damage!")
            return
        elif attack_roll == "Crit":
            damage, damage_type = self.calculate_damage(self.weapon, crit=True)
            var.output.append(f"{self.name} does {damage} {damage_type} damage!")
            target.take_damage(damage, damage_type)
        elif attack_roll >= target.AC:
            var.output.append(f"{target.name}'s AC is {target.AC}, so {self.name} hits {target.name}!")
            damage, damage_type = self.calculate_damage(self.weapon)
            var.output.append(f"{self.name} does {damage} {damage_type} damage!")
            target.take_damage(damage, damage_type)
        else:
            var.output.append(f"{self.name} misses {target.name}, and does no damage.")

    def make_off_hand_attack(self, target):
        var.output.append(f"{self.name} makes a bonus action attack against {target.name} with their {self.off_hand}.")
        attack_roll = self.make_attack_roll()
        if attack_roll == "Crit Fail":
            var.output.append(f"{self.name} rolls a 1 on their attack roll, critically failing the attack, "
                              f"and doing no damage!")
            return
        elif attack_roll == "Crit":
            damage, damage_type = self.calculate_damage(self.off_hand_weapon, crit=True, bonus=False)
            var.output.append(f"{self.name} does {damage} {damage_type} damage!")
            target.take_damage(damage, damage_type)
        elif attack_roll >= target.AC:
            var.output.append(f"{target.name}'s AC is {target.AC}, so {self.name} hits {target.name}!")
            damage, damage_type = self.calculate_damage(self.off_hand_weapon, bonus=False)
            var.output.append(f"{self.name} does {damage} {damage_type} damage!")
            target.take_damage(damage, damage_type)
        else:
            var.output.append(f"{self.name} misses {target.name}, and does no damage.")

    def make_attack_roll(self, advantage=False, disadvantage=False):
        if advantage and not disadvantage:
            r = max(d20(), d20())
        elif disadvantage and not advantage:
            r = min(d20(), d20())
        else:
            r = d20()
        if r == 1:
            return "Crit Fail"
        elif r == 20:
            var.output.append(f"{self.name} rolls a 20 on their attack roll, scoring a critical hit!")
            return "Crit"
        attack_roll = r + self.attack_bonus
        var.output.append(f"{self.name} rolls [{r}+{self.attack_bonus}] on their attack roll, "
                          f"for a total of {attack_roll}.")
        return attack_roll

    def calculate_damage(self, weapon, crit=False, bonus=True):
        rolls = weapon.roll_damage(crit)
        damage = sum(rolls)
        if bonus:
            damage += self.damage_bonus
            var.output.append(f"{self.name} rolls [{[x for x in rolls]} + {self.damage_bonus}], "
                            f"for a total of {damage} {weapon.damage_type} damage.")
        else:
            var.output.append(f"{self.name} rolls [{[x for x in rolls]}], "
                              f"for a total of {damage} {weapon.damage_type} damage.")
        return damage, weapon.damage_type

    def take_damage(self, damage, damage_type):
        if damage_type in self.invulnerabilities:
            damage = 0
        elif damage_type in self.resistances:
            damage = damage // 2
        elif damage_type in self.vulnerabilities:
            damage *= 2
        if self.HP > damage:
            self.HP -= damage
            var.output.append(f"{self.name} takes {damage} {damage_type} damage, and has {self.HP}HP remaining!")
        else:
            damage = self.HP
            var.output.append(f"{self.name} takes {damage} {damage_type} damage, and is reduced to 0HP!")
            self.HP = 0
            if ("Relentless Endurance" in self.features) and (self.uses['Relentless Endurance'] > 0):
                self.uses['Relentless Endurance'] -= 1
                self.HP = 1
                var.output.append(f"{self.name} uses their Relentless Endurance, and regains 1HP!")
            else:
                var.output.append(f"{self.name} dies!")



class Barbarian(Character):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.max_HP = 12 + self.con_mod + ((4 + self.con_mod) * (self.level - 1))
        self.features.append("Rage")
        self.uses['Rage'] = 2
        self.features.append("Unarmored Defense")
        if self.level >= 2:
            self.features.append("Reckless Attack")
            self.features.append("Danger Sense")
        if self.level >= 3:
            self.features.append("Frenzy")

    def set_max_HP(self):
        return 12 + self.con_mod + ((4 + self.con_mod) * (self.level - 1))

    def set_AC(self):
        if self.armor.name == "Unarmored":
            armor_class = (10 + self.dex_mod + self.con_mod)
        else:
            armor_class = super().set_AC()
        if self.off_hand == 'Shield':
            armor_class += 2
        return armor_class

    def __repr__(self):
        return f"""
                    {self.name} is a Level {self.level} Barbarian.
                    Max HP: {self.max_HP}
                    Strength: {self.str}
                    Dexterity: {self.dex}
                    Constitution: {self.con}
                    Armor: {self.armor.name}
                    AC: {self.AC}
                    Weapon: {self.weapon.name}

                """

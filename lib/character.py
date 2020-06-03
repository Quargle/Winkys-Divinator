#!/usr/bin/python3
# -*- coding: utf-8 -*-
#*****************************************************************************************
# DND_Duel_Classes_2.py
# Python 3
# Peter Evans, October 2018
# Sets up Classes for DND Duels
#********************************************************************************

"""
Features included are:
    Feats:
    Fighting Styles 
        Defensive
        Duellist
        Great Weapon Fighter

    Class Features:
        Barbarian Rage
        Fighter's Second Wind
        Fighter's Action Surge (L2)

    Race features:
        Half-Orc Relentless Endurance


Features not yet considered are:
    Great Weapon Master bonus damage
    Great Weapon Master bonus attack on crit
    Halfling Luck
    Monk bonus action unarmed strike
    Paladin's Divine Smite (L2)
    The monk's ability to run away from a fight
    Barbarian's  Reckless Attack (L2)
    Divine smite should not be subject to resistance from Barbarian's Rage - it is radiant damage
"""

# Standard Library imports
import random
import math
# local imports
from . import var



class Character:
    def __init__(self, name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features):
        self.name = name
        self.race = race
        self.DnD_class = DnD_class
        self.level = level
        self.weapon = weapon
        self.armor = armor
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.equipment = equipment
        self.features = features

        self.set_proficiency_bonus()
        self.str_mod = self.set_ability_modifier(self.strength)
        self.dex_mod = self.set_ability_modifier(self.dexterity)
        self.con_mod = self.set_ability_modifier(self.constitution)
        self.set_AC()
        self.set_max_HP()
        self.attacks = 1
        self.reset()

        if self.race == "Half-Orc":
            self.features.append("Relentless Endurance")
            self.features.append("Savage Attacks")

    def reset(self):
        self.HP = self.max_HP
        self.ability_status = []
        self.set_attack_bonus()
        self.set_damage_bonus()

    def set_max_HP(self):
        self.max_HP = (self.hit_die + self.con_mod)
        self.max_HP += int(((self.hit_die/2) + 1) + self.con_mod) * (self.level - 1)
        if "Tough" in self.features:
            self.max_HP += (2*self.level)

    def set_AC(self):
        self.AC = self.armor.base_AC + min(self.dex_mod, self.armor.max_dex_bonus)
        if "Shield" in self.equipment: self.AC += 2
        if "Ring of Protection" in self.equipment: self.AC += 1
        if "Defensive" in self.features: self.AC += 1
        if self.armor.name == "Integrated Plate":
            self.AC = 16 + self.proficiency_bonus 

    def set_proficiency_bonus(self):
        if (self.level < 5):
            self.proficiency_bonus = 2
        elif (self.level < 9):
            self.proficiency_bonus = 3
        elif (self.level < 13):
            self.proficiency_bonus = 4
        elif (self.level < 17):
            self.proficiency_bonus = 5
        else:
            self.proficiency_bonus = 6

    def set_ability_modifier(self, ability_score):
        ability_mod = (ability_score - 10)/2
        return math.floor(ability_mod)

    def set_attack_bonus(self):
        if "Finesse"  in self.weapon.properties: self.ability_mod = max(self.str_mod, self.dex_mod)
        else: self.ability_mod = self.str_mod
        self.attack_bonus = self.ability_mod + self.proficiency_bonus

    def set_damage_bonus(self):
        if "Finesse"  in self.weapon.properties: self.damage_bonus = max(self.str_mod, self.dex_mod)
        else: self.damage_bonus = self.str_mod
        if "Duellist" in self.features and "2-handed" not in self.weapon.properties: 
            self.damage_bonus += 2

    def show_details(self):
        print()
        print("**********************************************")
        if "Shield" in self.equipment:
            print("{} is a {} {}, armed with a {}, carrying a shield and wearing {}.".format(self.name, self.race, self.DnD_class, self.weapon.name, self.armor.name))
        else:
            print("{} is a {} {}, armed with a {} and wearing {}.".format(self.name, self.race, self.DnD_class, self.weapon.name, self.armor.name))
        print("AC: {}               Max HP: {}".format(self.AC, self.max_HP))
        print("Strength: {}         Strength Modifier: +{}".format(self.strength, self.str_mod))
        print("Dexterity: {}        Dexterity Modifier: +{}".format(self.dexterity, self.dex_mod)) 
        print("Constitution: {}     Constitution Modifier: +{}".format(self.constitution, self.con_mod)) 
        print("Features: {}" .format(self.features))

    def show_HP(attacker, defender):
        if var.verbosity == True:
            print("{} HP: {}    {} HP: {}".format(attacker.name, attacker.HP, defender.name, defender.HP))
            print()


    def roll_initiative(self):
        initiative = random.randint(1,20)
        if var.verbosity == True:
            print("{} rolls {} ({}+{}) for intitiative.".format(self.name, initiative+self.dex_mod, initiative, self.dex_mod))
        return initiative + self.dex_mod

    def take_turn(self, defender):
        self.attack(defender)

    def attack(self, defender):
        for i in range (self.attacks):
            if defender.HP > 0:
                if var.verbosity == True: 
                    print("\n{} is attacking {} with the {}.".format(self.name, defender.name, self.weapon.name))
                if "Great Weapon Master" in self.features: attack_bonus -= 5
                attack_roll, attack_bonus = self.make_attack_roll()
                result = self.determine_if_hit(attack_roll, attack_bonus, defender)
                if result == "hit": damage_roll, damage_bonus = self.determine_damage()
                elif result == "crit": damage_roll, damage_bonus = self.determine_crit_damage()
                elif result == "miss": continue
                if "Great Weapon Master" in self.features: damage_bonus += 10
                damage = damage_roll + damage_bonus
                if var.verbosity == True: 
                    print("{} does {} ({}+{}) damage.".format(self.name, damage, damage_roll, damage_bonus))
                defender.take_damage(damage)

    def determine_if_hit(self, attack_roll, bonus, defender):
        if attack_roll == 1:
            if var.verbosity == True:  
                print("{} rolls {} and scores a Critical Miss!".format(self.name, attack_roll))
            return "miss"
        elif attack_roll == 20:
            if var.verbosity == True: 
                print("{} rolls {} and scores a Critical Hit!".format(self.name, attack_roll))
            return "crit"
        elif attack_roll + bonus < defender.AC:
            if var.verbosity == True: 
                print("{} rolls {} ({}+{}) against an AC of {}, and misses.".format(self.name, attack_roll+bonus, attack_roll, bonus, defender.AC))
            return "miss"
        elif attack_roll + bonus >= defender.AC:
            if var.verbosity == True: 
                print("{} rolls {} ({}+{}) against an AC of {}, and hits.".format(self.name, attack_roll + bonus, attack_roll, bonus, defender.AC))
            return "hit"
        else:
            print("Something has gone wrong with the attack roll...")

    def make_attack_roll(self):
        return random.randint(1,20), self.attack_bonus

    def determine_damage(self):
        rolls = int(self.weapon.damage.split('d')[0])
        return self.damage_roll(rolls), self.damage_bonus

    def determine_crit_damage(self):
        rolls = 2*int(self.weapon.damage.split('d')[0])
        if "Savage Attacks" in self.features: rolls += 1
        return self.damage_roll(rolls), self.damage_bonus

    def damage_roll(self, rolls):
        max = int(self.weapon.damage.split('d')[1])
        total = 0
        for i in range (rolls):
            roll = random.randint(1, max)
            if (roll == 1 or roll == 2) and ("Great Weapon Fighting" in self.features):
                roll = random.randint(1, max)
            total += roll
        return total

    def take_damage(self, damage):
        if "Heavy Armor Master" in self.features:
            damage -= 3
        if (damage - self.HP) > self.max_HP:
            if var.verbosity == True: 
                print("{} is killed outright!".format(self.name))
            self.HP = 0
            return
        damage = min(damage, self.HP) 
        self.HP -= damage
        if self.HP == 0: 
            if var.verbosity == True: 
                print("{} takes {} damage and is knocked unconscious.".format(self.name, damage))
            self.relentless_endurance()
        else: 
            if var.verbosity == True: 
                print("{} takes {} damage.".format(self.name, damage))

    def relentless_endurance(self):
        if ("Relentless Endurance" in self.features) and ("Relentless Endurance used" not in self.ability_status):
            self.HP = 1
            if var.verbosity == True: 
                print("{} has Relentless Endurance, and gets back up with 1HP.".format(self.name))
            self.ability_status.append("Relentless Endurance used")



class Barbarian(Character):
    def __init__(self, name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features):
        self.hit_die = 12
        super().__init__(name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features)
        self.features.append("Unarmored Defense")
        self.features.append("Rage")
        if self.level >= 5:
            self.attacks = 2
        if self.level == 20:
            self.strength += 4
            self.constitution += 4 
            self.str_mod = self.set_ability_modifier(self.strength)
            self.con_mod = self.set_ability_modifier(self.constitution)
        if self.armor.name == "no armor":
            self.AC += self.con_mod
        self.reset()

    def reset(self):
        super().reset()
        if ("Raging" in self.ability_status): 
            self.ability_status.remove("Raging")
        self.turns_raging = 0
        self.set_rages()
        self.relentless_rage_DC = 10

    def set_rages(self):
        if self.level >=1: self.rages = 2
        if self.level >= 3: self.rages = 3
        if self.level >= 6: self.rages =4
        if self.level >= 12: self.rages = 5
        if self.level >= 17: self.rages = 6

    def take_turn(self, defender):
        if ("Raging" in self.ability_status):
            self.turns_raging += 1
        if (self.turns_raging == 10) and self.level < 15:
            self.end_rage()
        if self.raging == False and self.rages > 0:
            self.rage()
        super().take_turn(defender)

    def roll_initiative(self):
        if self.level >= 7:
            a = random.randint(1,20)
            b = random.randint(1,20)
            initiative =  max(a,b)
        else:
            initiative = random.randint(1,20)
        if var.verbosity == True:
            print("{} rolls {} ({}+{}) for intitiative.".format(self.name, initiative+self.dex_mod, initiative, self.dex_mod))
        return initiative + self.dex_mod



    def take_turn(self, defender):
        if ("Raging" not in self.ability_status):
            self.start_rage()
        self.attack(defender)

    def determine_crit_damage(self):
        rolls = 2*int(self.weapon.damage.split('d')[0])
        if "Savage Attacks" in self.features: rolls += 1
        if self.level >= 17: rolls += 3
        elif self.level >= 13: rolls += 2
        elif self.level >= 9: rolls += 1
        return self.damage_roll(rolls), self.damage_bonus

    def start_rage(self):
        self.ability_status.append("Raging")
        self.damage_bonus += 2
        self.turns_raging = 0
        self.rages -= 1
        if var.verbosity == True: print("{} rages.".format(self.name))

    def end_rage(self):
        self.ability_status.remove("Raging")
        self.damage_bonus -= 2
        if var.verbosity == True: print("{}'s rage ends.".format(self.name))

    def take_damage(self, damage):
        if "Raging" in self.ability_status:
            damage = math.floor(damage/2)
        if (damage - self.HP) > self.max_HP:
            if var.verbosity == True: 
                print("{} is killed outright!".format(self.name))
            self.HP = 0
            return
        damage = min(damage, self.HP) 
        self.HP -= damage
        if self.HP == 0: 
            if var.verbosity == True: 
                print("{} takes {} damage and is knocked unconscious.".format(self.name, damage))
            self.relentless_endurance()
            self.relentless_rage()
        else: 
            if var.verbosity == True: 
                print("{} takes {} damage.".format(self.name, damage))

    def relentless_rage(self):
        if self.HP == 0:    # because may have increased already by relentless endurance
            if (self.level >= 11) and ("Relentless Rage Used" not in self.ability_status) and ("Raging" in self.ability_status):
                if var.verbosity == True: 
                    print("{} attempts to use Relentless Rage to stay up...".format(self.name))
                nat_roll = random.randint(1,20)
                total_roll = nat_roll + self.con_mod
                if (total_roll >= self.relentless_rage_DC):
                    self.HP = 1
                    if var.verbosity == True: 
                        print("{} rolls {}+{} against a DC of {}, and gets back up with 1HP.".format(self.name, nat_roll, self.con_mod, self.relentless_rage_DC))
                else: 
                    if var.verbosity == True: 
                        print("{} rolls {}+{} against a DC of {}, and is not successful.".format(self.name, nat_roll, self.con_mod, self.relentless_rage_DC))
                self.relentless_rage_DC += 5

class Fighter(Character):
    # NB All fighters are assumed to be of the Champion subclass (because the others are too complicated to code)
    def __init__(self, name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features):
        self.hit_die = 10
        super().__init__(name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features)
        self.features.append("Second Wind")
        if self.level >= 2: self.features.append("Action Surge")
        if self.level >= 5:
            self.attacks = 2
        if self.level >= 11:
            self.attacks = 3
        if self.level == 20:
            self.attacks = 4

    def reset(self):
        super().reset()
        if self.level >= 2: self.action_surges = 1
        if self.level >= 17: self.action_surges = 2

    def take_turn(self, defender):
        if (self.HP < self.max_HP/2) and ("Second Wind" in self.features) and("Second Wind used" not in self.ability_status):
            self.use_second_wind()
        else:
            self.attack(defender)
        if self.action_surges >= 1:
            if var.verbosity == True: 
                print("\n{} uses Action Surge to take another action!".format(self.name))
            self.action_surges -= 1
            self.attack(defender)

    def determine_if_hit(self, attack_roll, bonus, defender):
        if attack_roll == 1:
            if var.verbosity == True:  
                print("{} rolls {} and scores a Critical Miss!".format(self.name, attack_roll))
            return "miss"
        elif (attack_roll == 20) or (attack_roll == 19 and self.level >= 3) or (attack_roll == 18 and self.level >= 15):
            if var.verbosity == True: 
                print("{} rolls {} and scores a Critical Hit!".format(self.name, attack_roll))
            return "crit"
        elif attack_roll + bonus < defender.AC:
            if var.verbosity == True: 
                print("{} rolls {} ({}+{}) against an AC of {}, and misses.".format(self.name, attack_roll+bonus, attack_roll, bonus, defender.AC))
            return "miss"
        elif attack_roll + bonus >= defender.AC:
            if var.verbosity == True: 
                print("{} rolls {} ({}+{}) against an AC of {}, and hits.".format(self.name, attack_roll + bonus, attack_roll, bonus, defender.AC))
            return "hit"
        else:
            print("Something has gone wrong with the attack roll...")

    def use_second_wind(self):
        #regain HP worth 1d10 + fighter level
        start_HP = self.HP
        regain = random.randint(1, 10) + self.level
        self.HP += regain
        if self.HP > self.max_HP:
            self.HP = self.max_HP
        self.ability_status.append("Second Wind used")
        if var.verbosity == True:
            print("{} uses Second Wind, regaining {} HP.".format(self.name, self.HP-start_HP))



class Paladin(Character):
    def __init__(self, name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features):
        self.hit_die = 10
        super().__init__(name, race, DnD_class, level, weapon, armor, strength, dexterity, constitution, equipment, features)
        self.reset()
        if self.level >= 5:
            self.attacks = 2

    def reset(self):
        super().reset()
        self.lay_on_hands_pool = self.level * 5
        self.set_L1_spell_slots()
        self.set_L2_spell_slots()
        self.L3_spell_slots = 0
        self.L4_spell_slots = 0
        self.L5_spell_slots = 0
        # Not yet set for level 3-5 speel slots (Character level 9 or higher)

    def set_L1_spell_slots(self):
        if self.level == 1: self.L1_spell_slots = 0
        elif self.level == 2: self.L1_spell_slots = 2
        elif self.level == 3 or self.level == 4: self.L1_spell_slots = 3
        else: self.L1_spell_slots = 4

    def set_L2_spell_slots(self):
        if self.level <= 4: self.L2_spell_slots = 0
        elif self.level == 5 or self.level == 6: self.L2_spell_slots = 2
        else: self.L2_spell_slots = 3

    def take_turn(self, defender):
        if (self.HP + self.lay_on_hands_pool) <= self.max_HP and (self.lay_on_hands_pool > 0): 
            self.lay_on_hands()
        else:
            self.attack(defender)

    def determine_damage(self):
        rolls = int(self.weapon.damage.split('d')[0])
        damage_rolled = self.damage_roll(rolls) + self.try_divine_smite("hit")
        return damage_rolled, self.damage_bonus

    def determine_crit_damage(self):
        rolls = 2*int(self.weapon.damage.split('d')[0])
        if "Savage Attacks" in self.features: rolls += 1
        damage_rolled = self.damage_roll(rolls) + self.try_divine_smite("crit")
        return damage_rolled, self.damage_bonus

    def lay_on_hands(self):
        self.HP += self.lay_on_hands_pool
        print("{} uses Lay on Hands, regaining {} HP.".format(self.name, self.lay_on_hands_pool))
        self.lay_on_hands_pool = 0

    def try_divine_smite(self, hit):
        smite = 0
        if self.L5_spell_slots > 0: level = 5
        elif self.L4_spell_slots > 0: level = 4
        elif self.L3_spell_slots > 0: level = 3
        elif self.L2_spell_slots > 0: 
            level = 2
            self.L2_spell_slots -= 1
        elif self.L1_spell_slots > 0: 
            level = 1
            self.L1_spell_slots -= 1
        else: return 0
        for i in range(level + 1):
            smite += random.randint(1,8)
        if hit == "crit":   # on a crit, roll these dice a second time
            for i in range(level + 1):
                smite += random.randint(1,8)
        if var.verbosity == True: 
            print("{} uses a level {} spell slot to Divine Smite, causing an extra {} radiant damage!".format(self.name, level, smite))
        return smite







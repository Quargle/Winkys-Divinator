
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class DuelForm(FlaskForm):
    char1_name = StringField("Name", default="Character 1")
    char1_class = SelectField("Class", choices=[
        "Fighter",
        "Barbarian",
        ])
    char1_level = SelectField("Level", choices=[
        1, 2, 3,
        ])
    char1_race = SelectField("Race", choices=[
        "Human",
        "Dragonborn",
        "Gnome",
        "Half-Orc",
        "Halfling",
        "Hill Dwarf",
        "High Elf",
        "Tiefling",
        ])
    char1_weapon = SelectField("Weapon", choices=[
        "Club",
        "Dagger",
        "Greatclub",
        "Handaxe",
        "Javelin",
        "Light Hammer",
        "Mace",
        "Quarterstaff",
        "Sickle",
        "Spear",
        "Battleaxe",
        "Flail",
        "Glaive",
        "Greataxe",
        "Greatsword",
        "Halberd",
        "Lance",
        "Longsword",
        "Maul",
        "Morningstar",
        "Pike",
        "Rapier",
        "Scimitar",
        "Shortsword",
        "Trident",
        "War Pick",
        "Warhammer",
        "Whip",
        "Unarmed_Strike",
        ],
        default="Longsword"
        )
    char1_armor = SelectField("Armor", choices=[
        "No Armor",
        "Padded",
        "Leather",
        "Studded Leather",
        "Hide",
        "Chain Shirt",
        "Scale Mail",
        "Breastplate",
        "Half Plate",
        "Ring Mail",
        "Chain Mail",
        "Split",
        "Plate",
        ],
         default="No Armor")

    char2_name = StringField("Name", default="Character 2")
    char2_class = SelectField("Class", choices=[
        "Fighter",
        "Barbarian",
        ])
    char2_level = SelectField("Level", choices=[
        1, 2, 3,
        ])
    char2_race = SelectField("Race", choices=[
        "Human",
        "Dragonborn",
        "Gnome",
        "Half-Orc",
        "Halfling",
        "Hill Dwarf",
        "High Elf",
        "Tiefling",
        ])
    char2_weapon = SelectField("Weapon", choices=[
        "Club",
        "Dagger",
        "Greatclub",
        "Handaxe",
        "Javelin",
        "Light Hammer",
        "Mace",
        "Quarterstaff",
        "Sickle",
        "Spear",
        "Battleaxe",
        "Flail",
        "Glaive",
        "Greataxe",
        "Greatsword",
        "Halberd",
        "Lance",
        "Longsword",
        "Maul",
        "Morningstar",
        "Pike",
        "Rapier",
        "Scimitar",
        "Shortsword",
        "Trident",
        "War Pick",
        "Warhammer",
        "Whip",
        "Unarmed_Strike",
        ],
        default="Longsword"
        )
    char2_armor = SelectField("Armor", choices=[
        "No Armor",
        "Padded",
        "Leather",
        "Studded Leather",
        "Hide",
        "Chain Shirt",
        "Scale Mail",
        "Breastplate",
        "Half Plate",
        "Ring Mail",
        "Chain Mail",
        "Split",
        "Plate",
        ],
        default="No Armor")

    submit = SubmitField("Begin")

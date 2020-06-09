
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, FormField


class CharacterForm(FlaskForm):
    char_name = StringField(label="Name")
    char_class = SelectField("Class", choices=[
        "Fighter",
        "Barbarian",
        ])
    level = SelectField("Level", choices=[
        1, 2, 3,
        ])
    race = SelectField("Race", choices=[
        "Human",
        "Dragonborn",
        "Gnome",
        "Half-Orc",
        "Halfling",
        "Hill Dwarf",
        "High Elf",
        "Tiefling",
        ])
    str = SelectField(
        "Strength",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
    dex = SelectField(
        "Dexterity",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16
        )
    con = SelectField("Constitution", choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16
        )
    weapon = SelectField("Primary Weapon", choices=[
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
        "Unarmed Strike",
        ],
        default="Longsword")
    off_hand = SelectField("Other Hand", choices=[
        "None",
        "Shield",
        "Club",
        "Dagger",
        "Handaxe",
        "Light Hammer",
        "Sickle",
        "Scimitar",
        "Shortsword",
        ],
        default="None",)
    armor = SelectField("Armor", choices=[
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
        "Splint Mail",
        "Full Plate",
        ],
        default="No Armor")


class DuelForm(FlaskForm):
    char1 = FormField(CharacterForm)
    char2 = FormField(CharacterForm)
    submit = SubmitField("Fight")



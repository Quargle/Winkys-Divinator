
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class DuelForm(FlaskForm):
    char1_name = StringField("Name", default="Character 1")
    char1_class = SelectField(
        "Class",
        choices=[
            "Fighter",
            "Barbarian",
            ]
        )
    char1_level = SelectField(
        "Level",
        choices=[1, 2, 3,]
        )
    char1_race = SelectField(
        "Race",
        choices=[
            "Human",
            "Dragonborn",
            "Gnome",
            "Half-Orc",
            "Halfling",
            "Hill Dwarf",
            "High Elf",
            "Tiefling",
        ])
    char1_str = SelectField(
        "Strength",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
    char1_dex = SelectField(
        "Dexterity",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
    char1_con = SelectField(
        "Constitution",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
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
        "Unarmed Strike",
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
        "Splint Mail",
        "Full Plate",
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
    char2_str = SelectField(
        "Strength",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
    char2_dex = SelectField(
        "Dexterity",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
    char2_con = SelectField(
        "Constitution",
        choices=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        default=16,
        )
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
        "Unarmed Strike",
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
        "Splint Mail",
        "Full Plate",
        ],
        default="No Armor")

    submit = SubmitField("Begin")


from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField


class DuelForm(FlaskForm):
    char1_name = StringField("Name")
    char1_class = SelectField("Class", choices=[
        "Fighter",
        "Barbarian",
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
        "Longsword",
        "Greatsword",
        "Rapier"
        ])

    char2_name = StringField("Name")
    char2_class = SelectField("Class", choices=[
        "Fighter",
        "Barbarian",
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
        "Longsword",
        "Greatsword",
        "Rapier"
        ])

    submit = SubmitField("Begin")
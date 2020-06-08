

var twoHandedWeapons = [
    "Greatclub",
     "Glaive",
     "Greataxe",
     "Greatsword",
     "Halberd",
     "Maul",
     "Pike"];

var lightWeapons = [
    "Club",
    "Dagger",
    "Handaxe",
    "Light Hammer",
    "Sickle",
    "Scimitar",
    "Shortsword"
    ];

let char1WeaponSelect = document.getElementById('char1-weapon');
let char2WeaponSelect = document.getElementById('char2-weapon');
let char1OffHand = document.getElementById('char1-off_hand');
let char2OffHand = document.getElementById('char2-off_hand');


char1WeaponSelect.onchange = function() {weaponSelectChange('char1', char1WeaponSelect.value)};
char2WeaponSelect.onchange = function() {weaponSelectChange('char2', char2WeaponSelect.value)};

function weaponSelectChange(char, choice) {
    if (lightWeapons.includes(choice)) {
        setLightWeaponChoices(char);
    } else if (twoHandedWeapons.includes(choice)) {
        setTwoHandedWeaponChoices(char);
    } else {
        setNormalWeaponChoices("char1");
    }
}

function setLightWeaponChoices(char) {
    // None, shield and all light weapons
    let optionHTML = '<option value="None">None</option>';
    optionHTML += '<option value="Shield">Shield</option>';
    for (let weapon of lightWeapons) {
        // add select option
        optionHTML += '<option value="' + weapon + '">' + weapon + '</option>';
        setOffHandChoices(char, optionHTML);
    }
}

function setTwoHandedWeaponChoices(char) {
    let optionHTML = '<option selected value="None">None</option>';
    setOffHandChoices(char, optionHTML);
}

function setNormalWeaponChoices(char) {
    // Just None and Shield
    let optionHTML = '<option value="None">None</option>';
    optionHTML += '<option value="Shield">Shield</option>';
    setOffHandChoices(char, optionHTML);
}

function setOffHandChoices(char, optionHTML) {
    if (char == "char1") {
        char1OffHand.innerHTML = optionHTML;
    } else if (char == "char2") {
        char2OffHand.innerHTML = optionHTML;
    }

}



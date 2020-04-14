
/* This file contains functions that are used when creating a character on Winky's Divinator  */


document.getElementById("class").addEventListener("change", classDescription);    // detects class choice & calls classDescritpion()
document.getElementById("race").addEventListener("change", raceDescription);    // detects race choice & calls raceDescritpion()

//document.getElementById("choice2").addEventListener("change", addChoice3);    // detects Option 2 choice & calls addChoice()

function classDescription() {addDescription("class", "classInfo", "character class")};
function raceDescription() {addDescription("race", "raceInfo", "race")};

 // This function adds text confirming one of your choices
function addDescription (question, choiceInfo, description) {
    choice = document.getElementById(question).value;
    document.getElementById(choiceInfo).innerHTML = "You have chosen a " + description + ": " + choice;
    };





/* This block displays an alert when the submit button is clicked */
document.getElementById("submitButton").addEventListener("click", function() {
    alert("You clicked the submit button!");
    });

/*
Adding Elements Dynamically

The addElement() function is simple if you understand its arguments. 
The way it works is by appending a new child element to a parent element. 
The parent element is specified using the parentId argument. 
The type of element to be created is specified using the elementTag argument. 
The new elements ID is specified using ths elementId argument. 
Lastly, the innerHTML of the new element is specified using the html argument.
*/
/* LEGACY CODE - PROBABLY NEVER REQUIRED.
function addChoice3() {

    // remove any previous version of this element you want to create
    if (document.getElementById("choice3") != null) {
        removeElement("choice3")
    };

    // get the necessary info for the new element
    var element = document.getElementById("choice2");
    var choice = element.value
    document.getElementById("classInfo").innerHTML = "You have made choice2: " + choice;
    var newElementId = "choice3";
    var newElementTag = "select";
    var newElementParent = element.parentNode;
    //html = "This is a new paragraph";
    
    // create the new element
    var newElement = document.createElement(newElementTag);
    newElement.setAttribute('id', newElementId);
    //newElement.innerHTML = html;
    newElementParent.appendChild(newElement);
};
*/

function removeElement(elementId) {
    // Removes an element from the document
    var element = document.getElementById(elementId);
    element.parentNode.removeChild(element);
};

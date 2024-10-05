// Function using ES5 version
// Define object with key and value
// Function without shorthand
function getPersionES5(name, age, height) {
    return {
        name: name,
        age: age,
        height: height,
        getheightInInches: function() {return height/2.54;}
    };
}
const person = getPersionES5("Chandra", 23, 172);
console.log("name of persion", person);
console.log("Height of the persion ", person.getheightInInches());

// Function using ES6 syntax
// Shorthand property
// Function with shorthand
// Computed property
const computedProperty = 'firstName';
function midName() {
    return 'middleName';
}
function getPersionES6(name, age, height) {
    return {
        name,
        age,
        height,
        [ computedProperty ]: name.split(' ')[0],
        [ midName() ]: name.split(' ')[1],
        [ 'last' + 'Name' ]: name.split(' ')[2],
        getheightInInches() {return height/2.54;}
    };
}
const person2 = getPersionES6("Chandra Kant Sharma", 23, 172);
console.log("Name of persion", person2);
console.log("Height of the persion ", person2.getheightInInches());

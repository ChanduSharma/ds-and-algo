const example = 3.14;

// Embed expressions 
console.log(`Example of template literal. Value of pi is ${example}`);

// Is multiline 
console.log(` Example of multiline string.
    This include multiple line
    This is also\n multiline`);

// Can be Escaped and embedded into other template literal
console.log(`This is ${`\`` === "`"}`);

// Tagged template literals
function tag(strings, radius) {
    const area = 3.14 * radius * radius;

    return strings[0] + radius.toString() + " and it's area is " + area.toString();
}

const radius = 23;

console.log(tag`Radius of circle is ${radius}`);
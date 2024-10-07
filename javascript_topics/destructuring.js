// Destructuring arrays 
// happens from left to right
const [name1, name2] = ['John', 'Michael'];
console.log(name2, name1);

// Variables less than array length then rest array discarded
const [num1 , num2] = [1, 2, 3, 4, 5];
console.log(num1, num2);

// Variables more than array lenght then rest variables are undefined.
const [num11 , num12, num13, num14, num15, num16] = [1, 2, 3, 4, 5];
console.log("variables more than array length.");
console.log(num11 , num12, num13, num14, num15, num16);
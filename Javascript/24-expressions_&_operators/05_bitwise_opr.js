// Bitwise operators treat arguments as 32-bit numbers and work on the level of their binary representation

let x = 4; // => 00000100
let y = 7; // => 00000111
let z = 2; // => 00000010

console.log(x & y); // 00000100 => 4 
console.log(y | x); // 00000111 => 7
console.log(x ^ y); // 00000011 => 3
console.log(~ y); // 11111000 => -8
console.log(y << x); // 01110000 => 112
console.log(x >> z); // 00000001 => 1
let a = -3; // 00000011
let b = 222225454288; // 11011111
console.log(a >>> b); // 000
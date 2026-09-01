// falsy values => false, 0, -0, 0n, "", NaN, undefined, null
// truthy values => everything except falsy values



console.log('-- falsy values --')

let falsy1; // this is undefined
if (falsy1) {
  console.log('truthy');
} else {
  console.log('falsy');
}

const falsy2 = 0;
if (falsy2) {
  console.log('truthy');
} else {
  console.log('falsy');
}

const falsy3 = 0n; // this is BigInt data type
if (falsy3) {
  console.log('truthy');
} else {
  console.log('falsy');
}

const falsy4 = '';
if (falsy4) {
  console.log('truthy')
} else {
  console.log('falsy')
}

const falsy5 = false;
if (falsy5) {
  console.log('truthy');
} else {
  console.log('falsy');
}

const falsy6 = 'apple' * 2; // its result is NaN but its type is Number
console.log(falsy6); // NaN
if (falsy6) {
  console.log('truthy');  
} else {
  console.log('falsy');
}

const falsy7 = null; // similar to none in python.
if (falsy7) {
  console.log('truthy');
} else {
  console.log('falsy');
}

const falsy8 = -0; // not normaly used
if (falsy8) {
  console.log('truthy');
} else {
  console.log('falsy');
}

console.log('-- truthy values --')

// truthy => ' ', '0', true, '-0', '0n'
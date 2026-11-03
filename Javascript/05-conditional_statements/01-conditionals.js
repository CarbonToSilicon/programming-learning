/*
const age = 120;

if (age >= 18) {
  console.log("You can drive");
}


if (age >= 18) {
  console.log('You can drive');
} else {
  console.log('You cannot drive');
}


if (age >= 18) {
  console.log('You can drive');
} else if (age >= 16) {
  console.log('You are almost aligible');
} else {
  console.log('You cannot drive')
}


if (age >= 120) {
  console.log('You are a god i bow you');  
} else if (age >= 18) {
  if (age >= 80) {
    console.log('It is too risky to drive');
  } else {
    console.log('You can drive');
  }
} else {
  console.log('You are not aligible to drive');
}


// ####### Some Popular if else shortcuts #######

// ternery statement

const result = 'tushar' ? 'truthy' : 'falsy';
console.log(result);

const result1 = (1 > 1 || 3 === '3') ? '"if" works' : '"else" works';
console.log(result1);

// guard operator, short circuit evaluation

let candidates = '';
candidates && console.log(`There are total ${candidates}.`)

const message = false && 'hello';
console.log(message);

// default operator

const mainCurrency = 'USD';
const Currency2 = null
const Currency = Currency2 || mainCurrency;
console.log(Currency);
*/


if (4>4) {
  console.log(true);
} else if (3==4) {
  console.log(true);
} else {
  console.log(false);
}

const god = 'Tushar I'

if (god.length <= 5) {
  console.log('small');
} else if (god.length < 6) {
  console.log('intermediate');
} else {
  console.log('big');
}

// npm install propmt-sync
// !----------------------------------!
const input = require('prompt-sync')();
let dayInput = input('Type a number value: ')

let day = parseInt(dayInput, 10);
console.log(day);
switch(day) {
  case 1:
    console.log('Monday')
    break
  case 2:
    console.log('Tuesday')
    break
  case 3:
    console.log('Wednesday')
    break
  case 4:
    console.log('Thursday')
    break
  case 5:
    console.log('Friday')
    break
  case 6:
    console.log('Saturday')
    break
  case 7:
    console.log('Sunday')
    break
  default:
    console.log('wrong input!');
}

const score = input('Enter your score between 0 to 100: ');
console.log(score);
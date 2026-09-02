
const age = 120;

/* if (age >= 18) {
  console.log("You can drive");
} */


/* if (age >= 18) {
  console.log('You can drive');
} else {
  console.log('You cannot drive');
} */


/* if (age >= 18) {
  console.log('You can drive');
} else if (age >= 16) {
  console.log('You are almost aligible');
} else {
  console.log('You cannot drive')
} */


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

const result = 0 ? 'truthy' : 'falsy';
console.log(result);

const result1 = (1 > 0 || 3 === '3') ? '"if" works' : '"else" works';
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
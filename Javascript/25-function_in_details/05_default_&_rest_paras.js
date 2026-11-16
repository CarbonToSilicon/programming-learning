// default parameters

function product(a, b) {
  b = typeof b != 'undefined'? b: 1;
  return a*b;
}

console.log(product(23, 2));
console.log(product(23));
console.log(product());

  // the better modern way to handle such an error
function product2(a = 0, b = 1) {
  return a*b;
}

console.log(product2(23, 2));
console.log(product2(23));
console.log(product2());


// rest parameters

 // the rest parameter syntax allows us to represent an indefinite number of arguments as an array
function multiply(multiplier, ...theArgs){
  console.log(Array.isArray(theArgs));
  return theArgs.map((x) => multiplier * x);
}

console.log(multiply(2, 1, 0, 3, 5, 7));
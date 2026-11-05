// let result = (expression1, expression2, ..., expressionN);

let x = 10;
let y = (x++, x + 1);
// parsed as: (let y = x++), (x + 1);
// result: y becomes 10, then x is incremented to 11, and the final value (12) is discarded.
console.log(y);

let u = (12, 3, 34);
// there is no expressions before the last comma then the last one will be chosen.
console.log(u);

let o = 4;
let r = (o++, 2, o + 5);
console.log(r);

// common use cases =>
for (let i=1, j=10; i<j; i++, j--) {
  console.log(`i: ${i}, j: ${j}`);
}


// comma operator vs. syntactic commas =>
// syntactic commas used in =>
// Array initializers - [1, 2, 3]
// Object Literals - {a: 1, b: 2, c: 3}
// Function Parameters - function multi(a, b) {}
// Function Arguments - multi(1, 3)
// Variable Declarations - let x = 1, y = 2;

// comma operator =>
// Explicit Expressions - let x = (1, 2);
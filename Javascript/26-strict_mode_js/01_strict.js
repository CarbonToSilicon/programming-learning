"use strict";

// Throws referenceError: userName is not defined
userName = "Alex";

// Throws SyntaxError: Duplicate parameter name not allowed
function add(a, a) {
  return a + a;
}
console.log(add(24, 34));

// 'this' is undefined instead of the window object
function checkThis() {
  console.log(this); // undefined
}

checkThis();
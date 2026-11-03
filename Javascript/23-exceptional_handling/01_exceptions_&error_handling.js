
// compile time error

  // syntax error
// console.log('b'

  // runtime error
// console.log(x);

try {
  console.log('Enterd try block.');
  console.log(x);
  console.log('Exit try block.');
    // network error
    // promise rejection
    // security errors

} catch(err) {
  console.log('One error catched -> ');
  console.log(err);
  console.error("Name:", err.name);       // Output: ReferenceError
  console.error("Message:", err.message); // Output: x is not defined
  console.error("Cause:", err.cause);     // Output: undefined
    // retry logic
    // fallback mechanism
    // logging
    // custom errors

} finally {            //optional
  // always executes
  console.log('Programe completed.');
    // close files
    // close connections
    // release resources
}

let input;
try {
  input = require('prompt-sync')();

} catch(err2) {
  console.log('Install prompt-sync \nnpm install prompt-sync')
}

try {
  const dividend = parseInt(input('Enter a dividend: '), 10);
  const divisor = parseInt(input('Enter a divisor: '), 10);
  if (divisor === 0) {
    throw new Error(`You can't divide by zero idiot!`);
    /* Throw Statement
The throw statement throws a user-defined exception. Execution of the current function will stop (the statements after throw won't be executed), and control will be passed to the first catch block in the call stack. If no catch block exists among caller functions, the program will terminate. (excerpt from MDN) */
  }
  console.log(dividend / divisor)

} catch(err3) {
  console.log(err3);
}
  

if (false) {
  console.log('Status fine.')
} else {
  throw new Error('Vulnerable error detected!');
}


console.log(`------won't print, program terminated------`)

function sum(){ // a variadic function that excepts unknown numbers of arguments like the Math.min()
  let sum = 0;
  for (let i = 0; i < arguments.length; i++){
    sum += arguments[i];
    console.log(arguments[i]);
  }
  console.log(arguments);
  return [sum, arguments];
}

console.log(`Sum -> ${sum(10, 20, 10, 20, 34)[0]}`);

function assign(a){
  arguments[0] = 'empty'; // each argument can be set or reset
  console.log(a);
  console.log(arguments)
}

assign(34, 23);




// pending 























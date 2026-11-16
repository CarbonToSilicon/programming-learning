
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


// with default perameters

function funcWithDefault(a = 22){
  console.log(arguments[0]);
  console.log(a);
  arguments[0] = 66;
  console.log(arguments[0]);
  console.log(a);
  a = 88;
  console.log(arguments[0]);
  console.log(a);
  console.log('\n');
}

funcWithDefault();
funcWithDefault(10);

function func(a) {
  arguments[0] = 99; // updating arguments[0] also updates a
  console.log(a);
}
func(10); // 99

function func2(a) {
  a = 99; // updating a also updates arguments[0]
  console.log(arguments[0]);
}
func2(10); // 99


// arguments is an array like object
function toArray(){
  const args0 = Array.prototype.slice.call(arguments);
  // or
  const args1 = Array.from(arguments);
  // or
  const args2 = [...arguments];
  return [args0, args1, args2];
}

const funcValue1 = toArray(23, 45, 45, 23);

console.log(funcValue1);
console.log(Array.isArray(funcValue1[0]));
console.log(Array.isArray(funcValue1[1]));
console.log(Array.isArray(funcValue1[2]));













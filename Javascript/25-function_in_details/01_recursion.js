/* // infinite recursion
let num = 1;
function recursive(n){
  console.log(`${n+1} This is a recursive function...`);
  num += 1;
  
  recursive(num); // function calling itself
  console.log('hello');
}
console.log(num);
recursive(num);
console.log(num);
*/ // code crashes due to stack overflow


function coding(num){
  // base condition
  if (num === 0) {
    console.log("coding has been done!");
    return
  } else{
    console.log("i am doing coding");
    coding(num-1);
  }
}
coding(6);


// factorial => 5! = 5*4*3*2*1 = 5*4! <- 4*3! <- 3*2! <- 2*1!
//           => n! n*(n-1)*(n-2)*(n-3)....1

function factorial(k){
  // base case - stopping condition
  if (k === 1){
    return 1
  }
  // recursive case - calling itself again
  return k * factorial(k-1);
}
console.log(factorial(5));

function allBinaryStrings(n){
  const result = [];
  const path = [];
  function backtrack(){
    if (path.length === n){
      result.push(path.join(''));
      return;
    }
    path.push('0');
    backtrack();
    path.pop();
    
    path.push('1');
    backtrack();
    path.pop();
  }
  backtrack();
  return result;
}
console.log(allBinaryStrings(4));


function sumDown(n) {
  if (n === 1) {
    return 1; // Base Case (The Stop Sign)
  }
  let smallerSum = sumDown(n - 1); // Recursive Call (PAUSE here!)
  return n + smallerSum;
}

console.log(sumDown(7));

function pow(x, n) {
  return (n == 1) ? x : (x * pow(x, n - 1));
}

console.log(pow(2, 4));

let company = { // the same object, compressed for brevity
  sales: [{name: 'John', salary: 1000}, {name: 'Alice', salary: 1600 }],
  development: {
    sites: [{name: 'Peter', salary: 2000}, {name: 'Alex', salary: 1800 }],
    internals: [{name: 'Jack', salary: 1300}]
  }
};

// The function to do the job
function sumSalaries(department) {
  if (Array.isArray(department)) { // case (1)
    return department.reduce((prev, current) => prev + current.salary, 0); // sum the array
  } else { // case (2)
    let sum = 0;
    for (let subdep of Object.values(department)) {
      sum += sumSalaries(subdep); // recursively call for subdepartments, sum the results
    }
    return sum;
  }
}

console.log(sumSalaries(company)); // 7700
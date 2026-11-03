// for (initialization, condition, iterator) {
 // task to do
// }

for (let i=1; i<=10; i++) {
  console.log(`${i} for`);
}

// initialization *optional
// while (condition) {
  // task to do
// }

let i = 1;
while (i<=10) {
  console.log(`while ${i}`);
  i++;
}

// initialization
// do {
  // task to do *it will run at least 1 time even if the condition is not right
// } while (condition)

let j = 11;
do {
  console.log('Condition did not match!');
  j++;
} while (j <= 10)

// some_data
// for (let val of some_data) {
  // do some task
// }

let str = "Manus Kumar Lal";
let op_str = "";
for (let chr of str) {
  op_str = chr + op_str;
}
console.log(op_str);

// some_data
// for (let key in some_data) {
  // do some task
// }

const data = {0:'M', 1:'a', 2:'n', 3:'u', 4:'s', 5:' ', 6:'K', 7:'u', 8:'m', 9:'a', 10:'r', 11:' ', 12:'L', 13:'a', 14:'l'}
let say = "";
for (let k in data) {
  say += data[k];
}
console.log(say);

// using break; and continue;

for (let p = 1; p <= 15; p++) {
    if (p === 3) {
        continue; // Correctly skips printing 3 and moves to p = 4
    }
    if (p > 5) {
        break; // Stops the loop entirely
    }
    console.log(p);
}

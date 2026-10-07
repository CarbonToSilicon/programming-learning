let myArray = [22, 36, 60];
console.log(myArray);  // [ 22, 36, 60 ]
console.log(myArray[0]);  // 22
console.log(typeof myArray);  // object
console.log(Array.isArray(myArray));  // true
console.log(Array.isArray(['hey', 'hello', 'hi']));  // true
myArray[0] = 10;
myArray[3] = 99;
console.log(myArray);  // [ 10, 36, 60, 99 ]
console.log(myArray.length);  // 4
myArray.push(100);
console.log(myArray);  // [ 10, 36, 60, 99, 100 ]
myArray.splice(0, 2);
console.log(myArray);  // [ 60, 99, 100 ]


for (let i=0; i < myArray.length; i++) {
  console.log(myArray[i]);
}

for (let item of myArray) {
  console.log(item);
}

let sum = 0;
for (item of myArray) {
  sum += item;
}
let avg = sum / myArray.length;
console.log(`The average of all values of myArray is ${avg}`);
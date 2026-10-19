let myArray = [22, 36, 60];
console.log(myArray);  // [ 22, 36, 60 ]
console.log(myArray[0]);  // 22
console.log(typeof myArray);  // object
console.log(Array.isArray(myArray));  // true
console.log(Array.isArray(['hey', 'hello', 'hi']));  // true
myArray[0] = 10;
myArray[3] = 99;
myArray[3] = 100;
console.log(myArray);  // [ 10, 36, 60, 99, 100 ]
console.log(myArray.length);  // 4

myArray.splice(0, 2);
console.log(myArray);  // [ 60, 99, 100 ]

console.log(myArray.pop()); // 100
console.log(myArray); // [ 60, 99 ]

console.log(myArray.push(34, 55, 543)); // 5
console.log(myArray); // [ 60, 99, 34, 55, 543 ]

console.log(myArray.shift()); // 60
console.log(myArray); // [ 99, 34, 55, 543 ]

console.log(myArray.unshift([12, 56])); // 5
console.log(myArray.unshift(6));  // 6
console.log(myArray.unshift(90, 76, 478, 1)); // 10
console.log(myArray); // [ 90, 76, 478, 1, 6, [ 12, 56 ], 99, 34, 55, 543 ]

const myArray2 = myArray.toSpliced(5, 1);

for (let i=0; i < myArray2.length; i++) {
  console.log(myArray2[i]);
}

for (let item of myArray2) {
  console.log(item);
}

let sum = 0;
for (item of myArray2) {
  sum += item;
}
let avg = sum / myArray2.length;
console.log(myArray2);
console.log(`The average of all values of myArray is ${avg}`);
let myArray = [22, 36, 60];
console.log(myArray);  // [ 22, 36, 60 ]
console.log(myArray[0]);  // 22
console.log(typeof myArray);  // object
console.log(Array.isArray(myArray));  // true
console.log(Array.isArray(['hey', 'hello', 'hi']));  // true
myArray[0] = 10;
myArray[3] = 99;
myArray[4] = 100;
console.log(myArray);  // [ 10, 36, 60, 99, 100 ]
console.log(myArray.length);  // 4

myArray.splice(0, 2);
console.log(myArray);  // [ 60, 99, 100 ]

console.log(myArray.pop()); // 100
console.log(myArray); // [ 60, 99 ]

console.log(myArray.push(34, 55, 543)); // 5
console.log( myArray[myArray.length] = 110 ); // 110
console.log(myArray); // [ 60, 99, 34, 55, 543, 110 ]

console.log(myArray.shift()); // 60
console.log(myArray); // [ 99, 34, 55, 543, 110 ]

console.log(myArray.unshift([12, 56])); // 6
console.log(myArray.unshift(6));  // 7
console.log(myArray.unshift(90, 76, 478, 1)); // 11
console.log(myArray); // [ 90, 76, 478, 1, 6, [ 12, 56 ], 99, 34, 55, 543, 110 ]

const myArray2 = myArray.toSpliced(5, 1);

console.log(myArray[0]); // 90
console.log(myArray[-1]); // undefined
console.log( myArray[myArray.length - 1] ); // 110

console.log( myArray.at(-1) ); // 110

  // array is also an object. its indexes are keys.
  // array is coppied by reference just like an object
let fruits = ['banana'];
let arr = fruits;
console.log( fruits === arr ); // true
arr.push("pear");
console.log(fruits); // [ 'banana', 'pear']

  // we can also use it the wrong way like an object
fruits = [];
fruits[9] = 5;
fruits.age = 24;
console.log(fruits); // [ <9 empty items>, 5, age: 24 ]
console.log(fruits.length); // 10
console.log(fruits[3]); // undefined
console.log(fruits[9]); // 5
console.log(fruits.age); // 24
// | it is irreversible to get back those values
let nums = [1, 2, 3, 4, 5];
nums.length = 2;
console.log(nums); // [1, 2]

// methods pop() and push() run faster than shift() and unshift()

// loops over array
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
};

// better use fo..of loop on multi item a variable
for (let fruit of fruits) {
  console.log(fruit);
  if (fruit === fruits.at(-1) ) {
    console.log(`The last item is ${fruit}!`); // 5
  };
};

// another way to create an array
let items = new Array(2);
console.log( items[0] );
console.log( items.length );

let num_matrix = [
  [1, 2, 3], 
  [4, 5, 6],
  [7, 8, 9]
]

console.log(num_matrix[2][0])

// toString
let arr2 = [1, 2, 3];
console.log(arr2);
console.log(arr2.toString());
console.log(String(arr2));
console.log(String(arr2) === '1,2,3');

console.log([] + 1);
console.log([1] + 1);
console.log([1, 2] + 1);

console.log('' + 1);
console.log('1' + 1);
console.log('1, 2' + 1);

let prices = [4, 8, 15, 16, 23, 42]

// forEach() method
prices.forEach((price, i, ar) => {
  ar[i] = price * 0.5;
  console.log(price);
  console.log( `=> ${ar[i]}` );
})
console.log(prices); // the original array changes

// .map() method
let rates = [2, 6, 21, 34, 5]
let N_rates = rates.map((rate, i, ar) => {
  console.log(i, ar, rates);
  return rate * 0.5;
})
console.log(N_rates);

let t_rates = rates.map(price => price * 0.25);
console.log(t_rates);

const products = [
  {name: "Laptop",     price: 499, color: "white"},
  {name: "Smartphone", price: 899, color: "black"},
  {name: "Headphone",  price: 50,  color: "grey"},
  {name: "Tablet",     price: 199, color: "white"},
  {name: "Keyboard",   price: 210, color: "blue"}
]

const discounts = products.map((product) => {
  return {name: product.name, price: product.price *= 0.5, color: product.color} //{
    // ...product,
    // price: product.price * 0.5
  //}
})
console.log(products);
console.log(discounts);

const catagorisedProducts = products.map(product => {
  let category;
  if (product.price < 100) category = "budget";
  else if (product.price < 400) category = "mid-range";
  else category = "premium";
  return { ...product, category };
})
console.log(catagorisedProducts);

// .filter() method
const points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
let n_points = points.filter(n => n > 4);
console.log(n_points);

n_points = points.filter(n => n % 2 === 0);
console.log(n_points);

n_points = points.filter(n => n/2 === 7);
console.log(n_points);

// const products = [
//   {name: "Laptop",     price: 249.5, color: "white"},
//   {name: "Smartphone", price: 449.5, color: "black"},
//   {name: "Headphone",  price: 25,  color: "grey"},
//   {name: "Tablet",     price: 99.5, color: "white"},
//   {name: "Keyboard",   price: 105, color: "blue"}
// ]

let affordableProducts = products.filter(product => product.price < 200)
console.log(affordableProducts);

affordableProducts = products.filter(product => product.name.includes("phone"))
console.log(affordableProducts);

affordableProducts = products.filter(product => {
  return product.color === "white" && product.price < 200} )
console.log(affordableProducts);

// .reduce() method

// const products = [
//   {name: "Laptop",     price: 249.5, color: "white"},
//   {name: "Smartphone", price: 449.5, color: "black"},
//   {name: "Headphone",  price: 25,  color: "grey"},
//   {name: "Tablet",     price: 99.5, color: "white"},
//   {name: "Keyboard",   price: 105, color: "blue"}
// ]

const totalPriceOfItems = products.reduce((accumulator, currentValue) => accumulator + currentValue.price, 0);
console.log(`$ ${totalPriceOfItems}`);

const words = ['Hello', ' ', 'world', '!', '\n']
console.log(words.reduce((statement, word) => statement + word, ''))

const fruitNames = ['apple', 'mango', 'orange', 'apple', 'orange', 'apple']
const frq_of_fruits = fruitNames.reduce((totalOccurence, currentFruit) => {
  if (!totalOccurence[currentFruit]) {
    totalOccurence[currentFruit] = 0;
  }
  totalOccurence[currentFruit] += 1;
  return totalOccurence},{})

console.log(frq_of_fruits)
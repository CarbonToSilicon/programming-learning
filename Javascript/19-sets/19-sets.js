let s =  new Set(); // A new, empty set
let t = new Set([1, s]); // A new set with two members
let unique = new Set('Mississippi');

console.log(s);
console.log(t);
console.log(unique);
console.log(unique.size); // it is like the length property of an array

let mS = new Set();
console.log(mS.size); // => 0
mS.add(1); // => add a number
console.log(mS.size); // => 1
mS.add(1); // add the same number again
console.log(mS.size); // => 1; the size does not change
mS.add(true); // it is fine to use mix types
console.log(mS.size); // => 2
mS.add([1, 2, 3]);
console.log(mS.size); // => 3; the array was added not its elements
console.log(mS);

console.log(mS.delete(1)); // value gets deleted if it exists
console.log(mS.size); // => 2; back to 2
console.log(mS); 
console.log(mS.delete('test')); // => false; "test" was not a member deletion failed
console.log(mS.delete(true)); // => true; deleted successfully
console.log(mS.delete([1, 2, 3])); // => false; the array in the set is different
console.log(mS.size); // => 1; there is that array in the set
console.log(mS); // => Set(1) { [1, 2, 3] }
mS.clear();
console.log(mS);
console.log(mS.size); // => 0

mS.add('a').add('b').add('c').add('d'); // chained methods
console.log(mS.size); // => 4
console.log(mS); // => Set(4) { 'a', 'b', 'c', 'd' }
mS.add([1, 2, 3]); 
mS.add([1, 2, 3]); // both arrays looks identical but both take distinct space in the memory
console.log(mS); // Set(6) { 'a', 'b', 'c', 'd', [ 1, 2, 3 ], [ 1, 2, 3 ] }

const primes = new Set([2, 3, 5, 7]); // Set() only takes one parameter
console.log(primes.has(3)); // => true; the set has the number
console.log(primes.has('5')); // => false; not even a number and it does not exist in the set
console.log(primes);

let sum = 0;
for (let p of primes) {
    sum += p;
}
console.log(sum);

console.log(Math.max(...primes));

let set2Array = [...primes];
console.log(Array.isArray(set2Array));
console.log(set2Array);

let product = 1;
primes.forEach(p => product *= p );
console.log(product);
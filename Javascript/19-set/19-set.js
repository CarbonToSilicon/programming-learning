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
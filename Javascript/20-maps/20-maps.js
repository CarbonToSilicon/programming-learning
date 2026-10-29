const myData = new Map(); // Map()

const name = 'tushar';
const myDict = {'die': 0};
const date = Symbol(13);



myData.set('apple', 20);
myData.set(34, '344');
myData.set(name, 19);
myData.set(myDict, myData.get('apple').toString());
myData.set(date, 'May');



console.log(myData); // print Map()

console.log(myData.get('apple'));
console.log(myData.get(34));
console.log(myData.get(name));
console.log(myData.get(myDict));
console.log(myData.get(date));


let m = new Map([
    ['one', 1],
    ['two', 2]
]);
m.set('three', 3);
console.log(m.get('two'));
console.log(m);

let copy = new Map(m);

let o = {'boys': 4, 'girls': 5};
let p = new Map(Object.entries(o)); // object to map
console.log(p);

console.log(p.delete('girls'));
console.log(p.has('girls'));
console.log(p.size);


p.clear();
console.log(p);

let c = new Map()
    .set('dog', 34)
    .set('git', true)
    .set(52, 'key');
console.log(c);

const r = new Map([['one', 1], ['one', 10]]);
console.log(r.size);
console.log(r);
console.log(typeof r); // object

const q = new Map([
    [{}, 12],
    [{}, 33]
]);
console.log(q.size);
console.log(q.get({})); // empty object is not a key

q.set(q, undefined);
console.log(q);

// Iteration follows insertion order; each item contains a key and value.
for (const [key, value] of myData) {
	console.log(key, value);
}

console.log(q.keys());
console.log(q.values());
console.log(q.entries());

const prices = new Map([
    ['apple', 3],
    ['banana', 2],
    ['cherry', 5]
]);

// const fruits = Object.fromEntries(prices.entries());
const fruits = Object.fromEntries(prices);

console.log(fruits);

// Use a Map for flexible key types, ordered entries, and easy size/iteration.
// Use an object for a simple record with fixed, string-named properties.

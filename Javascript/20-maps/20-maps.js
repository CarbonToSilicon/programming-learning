// A Map stores key-value pairs. Unlike a plain object, its keys can be any
// value, and it remembers the order in which entries were added.
const scores = new Map();

scores.set('Ada', 98); // Add an entry
scores.set('Linus', 91);
console.log(scores.get('Ada')); // 98: read an entry
console.log(scores); // Map(2) { 'Ada' => 98, 'Linus' => 91 }
console.log(typeof scores); // object

// Objects can be keys too. Object keys are matched by identity.
const user = { id: 1 };
scores.set(user, 'administrator');
console.log(scores.get(user)); // 'administrator'

console.log(scores.has('Linus')); // true
console.log(scores.size); // 3
scores.delete('Linus');

// Iteration follows insertion order; each item contains a key and value.
for (const [key, value] of scores) {
	console.log(key, value);
}

// Use a Map for flexible key types, ordered entries, and easy size/iteration.
// Use an object for a simple record with fixed, string-named properties.

// shorter funcitons

const a = ["Hydrogen", "Helium", "Lithium", "Beryllium"];

const a2 = a.map(function (s) {
  return s.length;
});
console.log(a2);

const a3 = a.map((s) => s.length);
console.log(a3)


const b = () => 34 * 3;
console.log(b());

const t = 13;
const c = a => a * 3;
console.log(c(t));

const d = 100;
const e = (a, b) => a + b;
console.log(e(t, d));
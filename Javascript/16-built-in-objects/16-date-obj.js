console.log(Date());

console.log(new Date());

console.log(Date('May 13 2006 12:43'));

let birthDate = new Date('May 13 2006 12:43');
console.log(birthDate);

let newDate = new Date(2006, 4, 13, 7+5, 13+30);
console.log(newDate);

console.log(newDate.getDay());
console.log(newDate.getFullYear());
console.log(newDate.getMonth());
console.log(newDate.getDate());
console.log(newDate.getHours('+0530'));
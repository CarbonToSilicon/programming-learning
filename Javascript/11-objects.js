
// Object

const Name = 'Tushar';
const surName = 'Bagora';

const product = {
    NAME: 'Tushar',
    age: 20,
    field: 'Programmer',
    languages: ['Python', 'HTML', 'CSS', 'Javascript', 'c++'],
    data: {
        education: 'Curently in BA III year',
        career: 'ML Engineer'
    },
    Fullname: `${Name} Bagora\n`
};

// Reading Data
console.log(product);
console.log('\n');
console.log(product.languages);
console.log('\n');
console.log(product.data.career);
console.log('\n');
console.log(product.languages[0]);
console.log('\n');

// Updating
product.NAME = 'NOT AVAILABLE'
console.log(product.NAME);
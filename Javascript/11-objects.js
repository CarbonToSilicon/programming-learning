
const Name = 'Tushar';
const surName = 'Bagora';

// Object
const product = {
    NAME: 'Tushar',
    compunding: true,
    age: 20,
    field: 'Programmer',
    languages: ['Python', 'HTML', 'CSS', 'Javascript', 'c++'],
    data: {
        education: 'Curently in BA III year',
        career: 'ML Engineer'
    },
    'Full-name': `${Name} Bagora\n`,
    func: function con_string() {
        console.log('Function inside an object');
    }
};

// Reading Data
console.log(product);
console.log(product.languages); // an item of dict. dot notation
console.log(product.data.career); // dict in dict
console.log(product.languages[0]); // array in dict
console.log(product['Full-name']); // bracket notation
product.func();
console.log(typeof product.func);
console.log(typeof console);
console.log(typeof console.log); // object + function = method

// Updating
product.NAME = 'NOT AVAILABLE'
console.log(product.NAME);

// Adding new item
product.newItem = 8529712390;
console.log(product.newItem);
console.log(product);

// Deleting an object item
delete product.newItem;
console.log(product.newItem); // if a value does not exist it is shown as undefined

//JSON
/* all key and value must use "" double quote is json.
   json does not support '' single quote.
   json does not support functions.
   json can be understood by almost every programming language.
   we use json to send and store data in a computer
*/

const normalObject = {
  name: 'Unkown',
  skill: 'python expert',
  married: false,
  moNumber: null,
  age: 20,
  marks: {
    english: 89,
    Python: 98,
  },
  interest: ['web devlopment', 'Machine Learning', 'software engineer']
}

console.log(typeof normalObject);

//  js object to JSON
jsonData = JSON.stringify(normalObject);
console.log(typeof jsonData);
console.log(jsonData);

// json to js object
jsObj = JSON.parse(jsonData);
console.log(jsObj);
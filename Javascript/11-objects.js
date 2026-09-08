
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

// auto-boxing
  // other  values can also have properties and methods
console.log('hello'.length);
console.log('hello'.toUpperCase());

  // we can update an object even when it is made using const
const object1 = {
  message1: 'hello!',
  message2: 'hello!',
  say: 'bey'
}

  // it is a reference (variable id) to another object and referece to another object is always equal to the original variable's reference
const object2 = object1;
console.log(object1 === object2);

const object3 = {
  message1: 'hello!',
  message2: 'hello!',
  say: 'bey'
}

  // we can't compare one object to another because those are just reference names
console.log(object1 === object3);
  // but we can compare one object's property to another object's property
console.log(object1.message1 === object3.message1);
console.log(object1.message2 === object3.message1);
console.log(object1.message2 === object3.say);

  // we can update a object and array's content when we are using const declaration because we are not changing the immediet reference
object1.message = 'good job!';
console.log(object1);

  // destructuring shortcut for -
// const message = object3.message1;
const { message1, message2, message_3 } = object3;
console.log(message1);
console.log(message2);
console.log(message_3);  // when we use defferent variable name than the property name it give undefined in the output

  // shorthand method
  // when a object property and the variable as value are same we can just write the variable name
const object4 = {
  // message1: message1
  message1,
  /*
  method: function func1() {
    console.log('go on');
  },
  */
  method() {
    console.log('go on');
  } 
}
console.log(object4);
object4.method();

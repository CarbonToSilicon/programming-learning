// JSON contains strings, numbers (eg. 10 1.2 -30 1.2e10), arrays (that only contains the data types listed here), null, booleans, objects (that only contains the data types listed here) *

const objData = {
    userName: "tushar3434",
    age: 20,
    isMarried: false,
    bankAcNo: null,
    interests: [ "cyber security", "rust ai ml", "web backend dev", 852, null, true, { at: "uk" }, [ 0 ] ],
    data: {project: "advanced systems"}
}

const jsonData = JSON.stringify(objData);

/*{"userName":"tushar3434","age":20,"isMarried":false,"bankAcNo":null,"interests":["cyber security","rust ai ml","web backend dev",852,null,true,{"at":"uk"},[0]],"data":{"project":"advanced systems"}}*/

console.log(jsonData);
const myJSON = `{
    "userName":"tushar3434",
    "age":20,
    "isMarried":false,
    "bankAcNo":null,
    "interests":["cyber security","rust ai ml","web backend dev",852,null,true,{"at":"uk"},[0]],
    "data":{"project":"advanced systems"}
}`
console.log(typeof jsonData);
console.log(typeof myJSON);

const toObjectData = JSON.parse(myJSON);
console.log(toObjectData);
console.log(typeof toObjectData);

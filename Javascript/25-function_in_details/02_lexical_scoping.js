
const myName = "Tushar";
function print(){
  console.log(myName);
  const hisName = "Kunal";
  function print1(){
    console.log(hisName);
    const herName = 'Abhishek';
    function print2(){
      console.log(herName);
    }
    print2();
  }
  print1();
  // function print3(){
  //   console.log(herName); can't access
  // }
  // print3();
  
  // console.log(herName); can't access
}

print();
// console.log(hisName); can't access
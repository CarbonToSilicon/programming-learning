// Boolean Values
 
// console.log(typeof true);
// console.log(typeof false);


// Comparison Operators

// console.log(3 > 5);
// console.log(3 > 5 - 3);

// console.log(7 < 7);
// console.log(7 <= 7);

// console.log(5 == '5.0')
// console.log(5 === '5.0')

// console.log(5 != '5.')
// console.log('5.1' != 5) // it first converts to number than compares but is not recommended
// console.log(5 !== '5.0')


// ------------------------------------------------------------

let data = [
  [1],  [ (undefined == undefined), (undefined == undefined), ( Object.is(undefined, undefined) ) ],
  [2],  [ (null == null), (null === null), ( Object.is(null, null) ) ],
  [3],  [ (true == true), (true === true), ( Object.is(true, true) ) ],
  [4],  [ (false == false), (false === false), ( Object.is(false, false) ) ],
  [5],  [ ('foo' == 'foo'), ('foo' === 'foo'), ( Object.is('foo', 'foo') ) ],
  [6],  [ (0==0), (0===0), ( Object.is(0, 0) ) ],
  [7],  [ (-0 == +0), (-0 === +0), ( Object.is(-0, +0) ) ],
  [8],  [ (+0 == 0), (+0 === 0), ( Object.is(+0, 0) ) ],
  [9],  [ (-0 == 0), (-0 === 0), ( Object.is(-0, 0) ) ],
  [10], [ (0n == -0n), (0n === -0n), ( Object.is(0n, -0n) ) ],
  [11], [ (0n == 0), (0n === 0), ( Object.is(0n, 0) ) ],
  [12], [ (0 == false), (0 === false), ( Object.is(0, false) ) ],
  [13], [ ("" == false), ("" === false), ( Object.is("", false) ) ],
  [14], [ ("" == 0), ("" === 0), ( Object.is("", 0) ) ],
  [15], [ ('0' == 0), ('0' === 0), ( Object.is('0', 0) ) ],
  [16], [ ('17' == 17), ('17' === 17), ( Object.is('17', 17) ) ],
  [17], [ (new String('foo') == 'foo'), (new String('foo') === 'foo'), ( Object.is(new String('foo'), 'foo') ) ],
  [18], [ (null == undefined), (null === undefined), ( Object.is(null, undefined) ) ],
  [19], [ (0 == NaN), (0 === NaN), ( Object.is(0, NaN) ) ],
  [20], [ (null == false), (null === false), ( Object.is(null, false) ) ],
  [21], [ (undefined == false), (undefined === false), ( Object.is(undefined, false) ) ],
  [22], [ (new String('f') == new String('f')), (new String('f') === new String('f')), ( Object.is(new String('f'), new String('f')) ) ],
  [23], [ (0 == null), (0 === null), ( Object.is(0, null) ) ],
  [], [ (NaN == NaN), (NaN === NaN), ( Object.is(NaN, NaN) ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
];

console.log(data);
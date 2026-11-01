// // Boolean Values
 
// console.log(typeof true);
// console.log(typeof false);


// // Comparison Operators

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
  [17], [ ([1, 2] == '1, 2'), ([1, 2] === '1, 2'), ( Object.is([1, 2], '1, 2') ) ],
  [18], [ (new String('foo') == 'foo'), (new String('foo') === 'foo'), ( Object.is(new String('foo'), 'foo') ) ],
  [19], [ (null == undefined), (null === undefined), ( Object.is(null, undefined) ) ],
  [20], [ (0 == NaN), (0 === NaN), ( Object.is(0, NaN) ) ],
  [21], [ (null == false), (null === false), ( Object.is(null, false) ) ],
  [22], [ (undefined == false), (undefined === false), ( Object.is(undefined, false) ) ],
  [23], [ ({foo: 'b'} == {foo: 'b'}), ({foo: 'b'} === {foo: 'b'}), ( Object.is({foo: 'b'}, {foo: 'b'}) ) ],
  [24], [ (new String('f') == new String('f')), (new String('f') === new String('f')), ( Object.is(new String('f'), new String('f')) ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]
  // [], [ ( == ), ( === ), ( Object.is() ) ]

];

console.log(data);
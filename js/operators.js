let x = 1;

x = -x;
console.log( x ); // -1, unary negation was applied

let y=3;
console.log( y - x ); // 4, binary minus subtracts values

console.log( 5 % 2 ); // 1, the remainder of 5 divided by 2

console.log( 2 ** 3 ); // 2³ = 8

console.log( 4 ** (1/2) ); // 2 (power of 1/2 is the same as a square root)

let s = "my" + "string";// concatination with binary +
console.log(s); // mystring 

console.log( '1' + 2 ); // "12"

console.log(2 + 2 + '1' ); // "41" and not "221"

console.log('2' + 2 + '1' ); 

console.log( 6 - '2' ); // 4, converts '2' to a number
console.log( '6' / '2' ); // 3, converts both operands to numbers

// No effect on numbers
let a = 1;
console.log( +a ); // 1

let by = -2;
console.log( +b ); // -2

// Converts non-numbers
console.log( +true ); // 1
console.log( +"" );   // 0

let apples = "2";
let oranges = "3";

console.log( apples + oranges ); // "23", the binary plus concatenates strings

let ants = "2";
let cats = "3";

// both values converted to numbers before the binary plus
console.log( +ants + +cats ); // 5

let p = 2 * 2 + 1;

alert( p ); // 5

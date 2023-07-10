let validAge;
let age = prompt('How old are you?', '');

if (age >= 18 ) {
  validAge = true;
} else {
  validAge = false;
}

alert("you are legally accepted? "+ validAge);

validAge = age < 13 ? true : false;
console.log("Below 13? "+validAge);

validAge = age > 65;
console.log("above 65? "+validAge);

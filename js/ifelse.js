let validAge;
let age = prompt('How old are you?', '');

if (age >= 18 ) {
  validAge = true;
} else {
  validAge = false;
}

alert("you are legally accepted? "+ validAge);
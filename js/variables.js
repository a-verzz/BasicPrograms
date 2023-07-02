let message;
message="hello"; // stores the string 'hello' in variable 'message'
alert(message); // will show variable content;

let user='John', 
    age='23', 
    messages='what\'s up';
console.log("user: "+user);
console.log("age: "+age);
console.log("message: "+messages);

//var was used in older javascripts instead of let

message="new Hello";
console.log("new message: "+message);

messages=message;
console.log("new messages: "+messages);
//one variable can be copied to other variables

//a variable name can not start with a number

// $ and _ can be used in naming a variable

// hyphen is not allowed in varible names

// without "use strict" mode, variables can be defined without let or var, as done in older versions of javascript. This method is not recommended

const FIX=007;

// this constant value will never change

// constants are generally in uppercase


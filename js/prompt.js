//format of confirm
//result = confirm(question);

let isCoder= confirm("Are you are coder?");
alert(isCoder+"  !!!!!");

// format of prompt
//result= prompt(title, [default]);

let age = prompt('How old are you?',100);
alert("Hello, you are "+age+" age old!!");

//if the promt value is not defined, it gives undefined error
let test = prompt("Test");
console.log("Test: "+test);

let tests = prompts("Tests",'');
alert("tests: "+ tests);


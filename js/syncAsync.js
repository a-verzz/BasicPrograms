// Synchronous Function
function syncFunction() {
    console.log("Synchronous function start");
    console.log("Performing a task...");
    console.log("Synchronous function end");
  }
  
  console.log("Before calling synchronous function");
  syncFunction();
  console.log("After calling synchronous function");
  
  // Asynchronous Function
  function asyncFunction() {
    console.log("Asynchronous function start");
    console.log("Performing a task...");
  
    setTimeout(() => {
      console.log("Asynchronous function end (after 2 seconds)");
    }, 2000);
  }
  
  console.log("Before calling asynchronous function");
  asyncFunction();
  console.log("After calling asynchronous function");
  
let firstName = null;
let lastName = null;
let nickName = "Supercoder";

// shows the first truthy value:
alert(firstName || lastName || nickName || "Anonymous"); // Supercoder



let firstNames = null;
let lastNames = null;
let nickNames = "Supercoder";

// shows the first truthy value:
alert(firstNames && lastNames && nickNames && "Anonymous"); // Supercoder


// let re = new RegExp("//", "gm");

// console.log(re);

// console.log(re.test("https://google.com"));

//Regular expression to check for comments in a C program

let re = new RegExp("///w*|/*/w**/", "gm");
console.log(re.test("//This is a comment"));
console.log(re.test("//This is a comment"));

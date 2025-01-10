/* //Variable and Data types

var x = 25; // This is not widely used but due hoisting property of the var.

let y = 20;

z = "Samridhha";

const name = "Aayusha";

const add = () => {
  let first = document.getElementById("first");
  let last = document.getElementById("last");
  let result = document.getElementById("result");
  console.log("This is working.");
  let val = parseInt(first.value) + parseInt(last.value);

  result.innerText = val;
};
 */

function getFactorial(n) {
  if (n == 0) {
    return 1;
  } else {
    return n * getFactorial(n - 1);
  }
}

function fact() {
  let num = prompt("Enter a number for factorial:");
  let result = getFactorial(num);
  alert(`The factorial of ${num} is ${result}`);
}

function getFibonacci(n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return getFibonacci(n - 1) + getFibonacci(n - 2);
  }
}

const fibo = () => {
  let num = prompt("Enter a number for fibonacci series:");
  let result = getFibonacci(num);
  alert(`The fibonacci of ${num} is ${result}`);
};

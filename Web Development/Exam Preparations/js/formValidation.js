/* var condition = /^([A-Za-z])\w/;
let name = "Animesh";
let result = name.match(condition);
if (result) {
  console.log("animesh".match(condition));
}
 */

// Design a from containing textbox for username, password, field for password, radio button for gender and checkfor for hobbies. WRite a program for client-side validation of the form for the user name and password field as required fields, lengtho f username should be 5, the radio button and checkbox should be checked.

function checkName(name) {
  let condition = /^([A-Za-z0-9]){5,}$/;
  let result = name.match(condition);
  if (result) {
    return true;
  } else {
    return false;
  }
}

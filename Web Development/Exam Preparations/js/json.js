let obj = {
  name: "Animesh",
  college: "Vedas College",
};

let str = JSON.stringify(obj);

console.log(str);

let obj1 = JSON.parse(str);

console.log(obj1);

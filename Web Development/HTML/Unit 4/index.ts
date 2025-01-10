
let input: any = document.getElementById("input");

let inputValue = parseInt(input?.value) || 0;

const fact = (n: number) => {
  if (n === 0) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
};

const factorial = () => {
  let result:any = document.getElementById("result");
  let val:number= fact(inputValue);
  result.innerText = val;
};

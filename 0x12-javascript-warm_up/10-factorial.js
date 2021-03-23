#!/usr/bin/node

const theNum = parseInt(process.argv[2]);

function factorial (num) {
  return num === 1 || isNaN(num) ? 1 : factorial(num - 1) * num;
}
console.log(factorial(theNum));

/*
let theNum = parseInt(process.argv[2]);
function factorial(num) {
if (num < 2 || isNaN(num)) {
return (1);
} else {
return ((factorial(num - 1) * num));
}
}
console.log(factorial(theNum));
*/

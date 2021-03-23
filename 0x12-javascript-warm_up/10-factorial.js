#!/usr/bin/node

const theNum = process.argv[2];

function factorial (num) {
  if (num === 1 || isNaN(num)) {
    return (1);
  } else {
    return parseInt((factorial(num - 1) * num));
  }
}
console.log(factorial(theNum));

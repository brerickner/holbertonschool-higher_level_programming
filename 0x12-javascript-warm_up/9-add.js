#!/usr/bin/node

const numOne = process.argv[2];
const numTwo = process.argv[3];
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
console.log(add(numOne, numTwo));

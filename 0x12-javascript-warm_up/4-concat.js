#!/usr/bin/node

const argLength = process.argv.length;
const argOne = process.argv[2];
const argTwo = process.argv[3];

argLength <= 2 || argLength >= 5 ? console.log('undefined is undefined') : argLength === 3 ? console.log(`${argOne}` + ' is undefined') : console.log(`${argOne}` + ' is ' + `${argTwo}`);

/* ______SAME AS______
if (argLength <= 2 || argLength >= 5 ){
console.log(`undefined is undefined`);
} else if (argLength === 3) {
  console.log(`${argOne}` + ' is undefined');
} else {
  console.log(`${argOne}` + ' is ' + `${argTwo}`);
}
*/

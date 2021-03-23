#!/usr/bin/node

const numArgs = process.argv;
const argLength = numArgs.length;

argLength < 4 ? console.log(0) : console.log(numArgs.sort()[argLength - 2]);

/*  ___SAME AS____
let numArgs = process.argv;
let argLength = numArgs.length;

if (argLength < 4) {
    console.log(0);
} else {
    console.log(numArgs.sort()[argLength - 2]);
}
*/

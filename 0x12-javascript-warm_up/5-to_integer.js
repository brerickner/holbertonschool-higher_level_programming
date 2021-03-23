#!/usr/bin/node

const theArg = parseInt(process.argv[2]);
isNaN(theArg) ? console.log('Not a number') : console.log('My number: ' + `${theArg}`);

/* ____SAME AS_____
if (isNaN(theArg)) {
console.log('Not a number');
} else {
console.log('My number: ' + `${theArg}`);
}
*/

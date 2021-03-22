#!/usr/bin/node

const argLength = process.argv.length;
argLength <= 2 ? console.log('No argument') : argLength === 3 ? console.log('Argument found') : console.log('Arguments found');

/* ______SAME AS______
let argLength = process.argv.length;
if (argLength <= 2) {
    console.log('No argument');
} else if (argLength == 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
*/

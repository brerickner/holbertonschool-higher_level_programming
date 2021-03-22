#!/usr/bin/node

const theArg = process.argv[2];
theArg === undefined ? console.log('No argument') : console.log(theArg);

/* ____SAME AS _____
if (theArg === undefined) {
  console.log('No argument');
} else {
  console.log(theArg);
}
*/

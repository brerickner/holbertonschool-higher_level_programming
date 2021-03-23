#!/usr/bin/node

const cStr = 'C is fun';
const x = process.argv[2];

if (isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x; i++) {
  console.log(`${cStr}`);
}

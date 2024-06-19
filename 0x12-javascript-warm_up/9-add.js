#!/usr/bin/node

const args = process.argv.slice(2);

const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

if (num2 === undefined || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}

function add (a, b) {
  return (a + b);
}

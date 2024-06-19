#!/usr/bin/node

const arg = process.argv.slice(2);
const num = arg[0];

if (num === undefined || isNaN(num)){
  console.log(1);
} else {
  console.log(factorial(num));
}

function factorial (x) {
  if (x <= 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (x === undefined || isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let result = '';
    for (let j = 0; j < x; j++) {
      result += 'X';
    }
    console.log(result);
  }
}

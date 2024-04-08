#!/usr/bin/node

const def = 'undefined';
const seperator = ' is ';

if (!process.argv[2]) {
  console.log(def.concat(seperator, def));
} else if (process.argv[2] && !process.argv[3]) {
  console.log(process.argv[2].concat(seperator, def));
} else {
  console.log(process.argv[2].concat(seperator, process.argv[3]));
}

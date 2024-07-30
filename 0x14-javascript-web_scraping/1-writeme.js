#!/usr/bin/node

const fs = require('fs');

/* A script that writes a string into a file */

if (process.argv.length < 4) {
  console.error('Please provide a file path and a string to write as arguments.');
  process.exit(1);
}

const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});

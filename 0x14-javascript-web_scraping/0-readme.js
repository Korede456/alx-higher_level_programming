#!/usr/bin/env node

const fs = require('fs');

/* A script that reads and prints the content of a file. */

if (process.argv.length < 3) {
  console.error('Please provide a file path as the first argument.');
  process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

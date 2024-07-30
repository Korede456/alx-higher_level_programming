#!/usr/bin/env node

const request = require('request');
const fs = require('fs');

if (process.argv.length < 4) {
  console.error('Pls enter a request url and a file path');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});

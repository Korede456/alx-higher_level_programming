#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide an api url.');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const completed = JSON.parse(body);
  console.log(completed);
});

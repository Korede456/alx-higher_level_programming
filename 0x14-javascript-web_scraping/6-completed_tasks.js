#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide an api url.');
  process.exit(1);
}

const url = process.argv[2];

request.get(url, { json:true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const completed = {};
  body.forEach((todo) => {
    if (todo.completed) {
      completed[todo.userId] = 1;
    } else {
      completed[todo.userId] += 1;
    }
  });
  console.log(completed);
});

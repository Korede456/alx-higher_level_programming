#!/usr/bin/env node

const request = require('request');

/* A script that prints the title of a star wars movie */

if (process.argv.length < 3) {
  console.error('Please provide an ID.');
  process.exit(1);
}

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movie = JSON.parse(body);
  console.log(movie.title);
});

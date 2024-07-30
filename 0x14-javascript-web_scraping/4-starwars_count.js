#!/usr/bin/env node

const request = require('request');

/* Prints the numver of movies where "Wedge Antilles" is present. */

if (process.argv.length < 3) {
  console.error('Please provide an api url.');
  process.exit(1);
}

const url = process.argv[2];
const wedgeAntillesId = '18';

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movies = JSON.parse(body);
  let count = 0;
  movies.results.forEach((movie) => {
    movie.characters.forEach((character) => {
      if (character.includes(wedgeAntillesId)) {
        count += 1;
      }
    });
  });
  console.log(count);
});

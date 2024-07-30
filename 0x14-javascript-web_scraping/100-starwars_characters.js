#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Please provide an ID.');
  process.exit(1);
}

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const characters = body.characters;
  characters.forEach((character) => {
    request.get(character, { json: true }, (error, response, body) => {
      if (error) {
        console.error(error);
      }
      console.log(body.name);
    });
  });
});

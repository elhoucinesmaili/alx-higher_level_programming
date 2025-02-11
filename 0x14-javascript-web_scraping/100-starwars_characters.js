#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  try {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (err, res, charBody) => {
        if (err) {
          console.log(err);
          return;
        }
        console.log(JSON.parse(charBody).name);
      });
    });
  } catch (err) {
    console.log(err);
  }
});

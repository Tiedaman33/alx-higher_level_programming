#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./getStarWarsMovie.js <movie ID>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Received status code ${response.statusCode}`);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});

#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);
  // Printing status code
  const FilmResults = JSON.parse(body).results;
  let meow = 0;
  for (let i = 0; i < FilmResults.length; i++) {
    for (let j = 0; j < FilmResults[i].characters.length; j++) {
      if (FilmResults[i].characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
        meow += 1;
      }
    }
  }
  console.log(meow);
});

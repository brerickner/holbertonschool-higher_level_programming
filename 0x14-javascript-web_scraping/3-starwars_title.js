#!/usr/bin/node
const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);
  // Printing status code
  console.log(JSON.parse(body).title);
});

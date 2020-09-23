#!/usr/bin/node
/*  script that prints all characters of a Star Wars movie */
const fs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (const movie of data.characters) {
    fs(movie, function (errr, responsee, bodyy) {
      console.log(JSON.parse(bodyy).name);
    });
  }
});

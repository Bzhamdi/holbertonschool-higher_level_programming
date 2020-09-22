#!/usr/bin/node
/*  script that prints the title  of a GET request. */
const fs = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});

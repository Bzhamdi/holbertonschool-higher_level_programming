#!/usr/bin/node
/*  script that prints foreach of a GET request. */
const fs = require('request');
const url = process.argv[2];
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  let sum = 0;

  for (const movie of data.results) {
    for (const char of movie.characters) {
      if (char.endsWith('/18/')) {
        sum++;
      }
    }
  }

  console.log(sum);
});

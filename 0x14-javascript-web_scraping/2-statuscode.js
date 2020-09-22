#!/usr/bin/node
/*  script that display the status code of a GET request. */
const fs = require('request');
fs(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  }
  console.log('code:', response.statusCode);
});

#!/usr/bin/node
/*  script that prints foreach of a GET request. */
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
req(url, function (errr, response, body) {
  fs.writeFile(filename, body, 'utf8', function (err, data) {
    if (err || data) {
      console.log(err || data);
    }
  });
});

#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err_description, err_data) {
  if (err_description || err_data) {
    console.log(err_description || err_data);
  } 
});

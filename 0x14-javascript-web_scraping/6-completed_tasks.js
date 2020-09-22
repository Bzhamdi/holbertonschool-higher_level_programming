#!/usr/bin/node
/*  script that computes the number of tasks completed by user id. */
const fs = require('request');
const url = process.argv[2];
const dict = {};
fs(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  for (const todo of data) {
    if (todo.completed === true) {
      if (dict[todo.userId] === undefined) {
        dict[todo.userId] = 1;
      } else {
        dict[todo.userId]++;
      }
    }
  }
  console.log(dict);
});

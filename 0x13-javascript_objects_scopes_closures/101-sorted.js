#!/usr/bin/node
/* dict groupe by key */
const dict = require('./101-data.js').dict;
const sort = {};
for (const key in dict) {
  if (!sort[dict[key]]) {
    sort[dict[key]] = [];
  }

  sort[dict[key]].push(key);
}
console.log(sort);

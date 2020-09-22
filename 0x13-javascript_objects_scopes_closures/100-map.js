#!/usr/bin/node
/* map use item and index */
const array1 = require('./100-data.js').list;
console.log(array1);
const map1 = array1.map((x, y) => x * y);
console.log(map1);

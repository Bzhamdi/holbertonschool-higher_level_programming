#!/usr/bin/node
/* js is a number */
if (isNaN(process.argv[2]) === false) {
  console.log('My number: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}

#!/usr/bin/node
/* js is a number */
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
#!/usr/bin/node
/* js is a number */

if (process.argv.length < 4) {
  console.log(1);
} else {
  let max = process.argv[2];
  let max2 = process.argv[2];
  for (let i = 3; i <= process.argv.length; i++) {
    if (process.argv[i] > max) {
      max = process.argv[i];
    }
  }
  for (let j = 3; j <= process.argv.length; j++) {
    if (process.argv[j] > max2 && process.argv[j] < max) {
      max2 = process.argv[j];
    }
  }
  console.log(max2);
}

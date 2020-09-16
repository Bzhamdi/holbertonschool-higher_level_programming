#!/usr/bin/node
/* js is a number */

if (process.argv.length === 4) {
  if ((parseInt(process.argv[2]) > parseInt(process.argv[3]))) {
    console.log(process.argv[3]);
  } else {
    console.log(process.argv[2]);
  }
}

if (process.argv.length < 4) {
  console.log(0);
} else if (process.argv.length > 4) {
  let max = process.argv[2];
  let max2 = process.argv[2];
  for (let i = 3; i <= process.argv.length; i++) {
    if (parseInt(process.argv[i]) > parseInt(max)) {
      max = process.argv[i];
    }
  }
  for (let j = 3; j <= process.argv.length; j++) {
    if (process.argv[j] > max2 && process.argv[j] < max) {
      max2 = parseInt(process.argv[j]);
    }
  }
  console.log(max2);
}

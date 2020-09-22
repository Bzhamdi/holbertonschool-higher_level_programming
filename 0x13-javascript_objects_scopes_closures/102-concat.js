#!/usr/bin/node
let fs = require('fs');
fs.writeFile(process.argv[4], fs.readFileSync(process.argv[2])+fs.readFileSync(process.argv[3]));
